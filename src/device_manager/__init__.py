#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:06
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
import os
import time

import flask
from flask_login import current_user

from config import config
from device_manager.models.device import Device
from device_manager.models.user import User
from device_manager.plugins.extensions import db, login_manager, mail, migrate


class ReverseProxied(object):
    # Flask url_for generating http URL instead of https
    # https://stackoverflow.com/questions/14810795/flask-url-for-generating-http-url-instead-of-https

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = environ.get('HTTP_X_API_SCHEME')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'production')

    app = flask.Flask(__name__, static_url_path='', instance_relative_config=True)
    app.wsgi_app = ReverseProxied(app.wsgi_app)

    app.config.from_object(config[config_name])
    app.config.from_pyfile(f'{config_name}.py')

    register_extensions(app)
    register_blueprints(app)
    register_template_context(app)

    return app


def register_extensions(app):
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    db.init_app(app)
    login_manager.init_app(app)
    register_shell_context(app)
    # from device_manager.plugins.extensions import compress
    # compress.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from device_manager.views import register_views
    register_views(app)

    from device_manager.plugins.admin import admin
    admin.init_app(app)


def register_template_context(app):
    @app.before_request
    def before_request():
        if current_user.is_authenticated:
            current_user.ping()
        flask.g.start_time = time.time()

    @app.after_request
    def after_request(response):
        if ('Content-Length' in response.headers):
            response.headers.add('Uncompressed-Content-Length', response.headers['Content-Length'])
        start_to_stop_time = time.time() - flask.g.start_time
        response.headers.add('Response-Time', round(start_to_stop_time, 3))
        return response

    @app.template_filter('my_split')
    def my_split(this, string, num):
        return str(this).split(string)[num]


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, Device=Device)

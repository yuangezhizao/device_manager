#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:17
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
# from flask_compress import Compress
from flask_login import LoginManager, AnonymousUserMixin
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()
# compress = Compress()
mail = Mail()
moment = Moment()
migrate = Migrate()


@login_manager.user_loader
def load_user(user_id):
    from device_manager.models.user import User
    return User.query.get(int(user_id))


login_manager.session_protection = 'strong'
login_manager.login_view = 'main.auth_index'
login_manager.login_message = '未授权用户，请先登录！'
login_manager.login_message_category = 'negative'


class Guest(AnonymousUserMixin):

    def can(self, permission_name):
        return False

    @property
    def is_admin(self):
        return False


login_manager.anonymous_user = Guest

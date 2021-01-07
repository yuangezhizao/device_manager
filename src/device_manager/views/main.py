#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:10
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
import flask
from flask_login import login_user, logout_user, login_required, current_user

from device_manager.models.device import Device
from device_manager.models.user import User

app = flask.current_app
bp = flask.Blueprint('main', __name__)


@bp.route('/')
def site_index():
    return flask.render_template('index.html')


@bp.route('/auth/index', methods=['GET', 'POST'])
def auth_index():
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('bp.site_index'))
    if flask.request.method == 'POST':
        username = flask.request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if user is None:
            flask.flash('不存在的用户名！', 'negative')
        elif not user.validate_password(flask.request.form['password']):
            flask.flash('不正确的密码！', 'negative')
        else:
            remember = flask.request.form.get('remember', False)
            login_user(user, remember)
            return flask.redirect(flask.url_for('bp.site_index'))
    return flask.render_template('auth/index.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flask.flash('注销成功！', 'info')
    return flask.redirect(flask.url_for('bp.auth_index'))


@bp.route('/transfer/index')
def transfer_index():
    transfer_index_data = Device.query.order_by(Device.id.asc()).all()
    return flask.render_template('transfer/index.html', transfer_index_data=transfer_index_data)


@bp.route('/transfer/device')
def transfer_device():
    serial = flask.request.args.get('serial')
    transfer_device_data = Device.query.filter_by(serial=serial).first_or_404()
    return flask.render_template('transfer/device.html', transfer_device_data=transfer_device_data)


@bp.route('/manage/index')
def manage_index():
    manage_index_data = Device.query.order_by(Device.id.asc()).all()
    return flask.render_template('manage/index.html', manage_index_data=manage_index_data)

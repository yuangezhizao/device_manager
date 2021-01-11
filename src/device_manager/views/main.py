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
from device_manager.plugins.send_email import send_transfer_email, send_confirm_email

app = flask.current_app
bp = flask.Blueprint('main', __name__)


@bp.route('/')
def site_index():
    # from device_manager.plugins.extensions import db
    # db.create_all()
    if current_user.is_authenticated:
        my_now_device_data = Device.query.filter_by(now_person=current_user).order_by(Device.id.asc()).all()
        my_next_device_data = Device.query.filter_by(next_person=current_user).order_by(Device.id.asc()).all()
        return flask.render_template('index.html', my_now_device_data=my_now_device_data,
                                     my_next_device_data=my_next_device_data)
    return flask.render_template('index.html')


@bp.route('/auth/index', methods=['GET', 'POST'])
def auth_index():
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('main.site_index'))
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
            return flask.redirect(flask.url_for('main.site_index'))
    return flask.render_template('auth/index.html')


@bp.route('/auth/logout')
@login_required
def auth_logout():
    logout_user()
    flask.flash('注销成功！', 'info')
    return flask.redirect(flask.url_for('main.auth_index'))


@bp.route('/transfer/device', methods=['GET', 'POST'])
@login_required
def transfer_device():
    serial = flask.request.args.get('serial')
    transfer_device_data = Device.query.filter_by(serial=serial).first_or_404()
    if flask.request.method == 'POST':
        func = flask.request.form.get('func')
        if func == 'start_transfer':
            if transfer_device_data.now_person != current_user:
                return '这已经不是你的设备了'
            next_user_id = flask.request.form.get('next_user')
            next_user = User.query.filter_by(username=next_user_id).first_or_404()
            transfer_device_data.next_person = next_user
            transfer_device_data.save()
            try:
                send_transfer_email(serial, next_user.email, current_user.email)
            except Exception as e:
                print(e)
            return flask.redirect(flask.url_for('main.transfer_device', serial=serial))
        elif func == 'stop_transfer':
            transfer_confirm = flask.request.form.get('transfer_confirm')
            if transfer_confirm:
                if transfer_device_data.next_person != current_user:
                    return '此设备并不需要你进行确认'
                next_user = transfer_device_data.next_person
                now_person = transfer_device_data.now_person
                # 邮件提醒
                transfer_device_data.now_person = next_user
                transfer_device_data.next_person = None
                transfer_device_data.save()
                try:
                    send_confirm_email(serial, now_person.email, current_user.email)
                except Exception as e:
                    print(e)
                if 'transfer' not in flask.request.referrer:
                    return flask.redirect(flask.url_for('main.site_index'))
                return flask.redirect(flask.url_for('main.transfer_device', serial=serial))
    user_all = User.query.order_by(User.id.asc()).all()
    return flask.render_template('transfer/device.html', transfer_device_data=transfer_device_data, user_all=user_all)


@bp.route('/manage/index')
@login_required
def manage_index():
    manage_index_data = Device.query.order_by(Device.id.asc()).all()
    return flask.render_template('manage/index.html', manage_index_data=manage_index_data)


@bp.route('/report')
def report():
    serial = flask.request.args.get('serial')
    status = int(flask.request.args.get('status', 1))
    device = Device.query.filter_by(serial=serial).first_or_404()
    device.device_online_status = status
    device.save()
    return f'序列号为【{serial}】的 CANoe 设备在线状态已更新为：{status}'

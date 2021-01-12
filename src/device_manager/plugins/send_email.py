#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2021/1/9 13:04
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
from threading import Thread

import flask
from flask_mail import Message

from device_manager.plugins.extensions import mail


def async_send_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_transfer_email(serial, recipients, cc):
    msg = Message('CANoe 设备转移开始提醒',
                  sender=('ALSI ES CANoe 设备管理系统', 'chenyuan.gao@alsi.cn'),
                  recipients=[recipients],
                  cc=cc)
    msg.body = f'序列号为【{serial}】的 CANoe 设备开始转移，请及时确认！详情请参照：http://10.30.10.216:5000/transfer/device?serial={serial}'
    app = flask.current_app._get_current_object()
    thread = Thread(target=async_send_mail, args=(app, msg))
    thread.start()


def send_confirm_email(serial, recipients, cc):
    msg = Message('CANoe 设备转移结束提醒',
                  sender=('ALSI ES CANoe 设备管理系统', 'chenyuan.gao@alsi.cn'),
                  recipients=[recipients],
                  cc=cc)
    msg.body = f'序列号为【{serial}】的 CANoe 设备已转移结束。详情请参照：http://10.30.10.216:5000/transfer/device?serial={serial}'
    app = flask.current_app._get_current_object()
    thread = Thread(target=async_send_mail, args=(app, msg))
    thread.start()

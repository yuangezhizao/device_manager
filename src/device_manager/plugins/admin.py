#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2021/1/9 10:09
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import flask
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from device_manager.models.device import Device
from device_manager.models.user import User
from device_manager.plugins.extensions import db

app = flask.current_app


class AdminIndexViewAuth(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.username in ('ASDL1B1DL033', 'ASDL1B8DL002'):
                return True
            else:
                return False
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return flask.redirect(flask.url_for('main.auth_index'))


class DeviceModelViewAuth(ModelView):
    column_display_pk = True
    column_labels = dict(id='No.', type='设备类型', serial='设备序列号', customer='顾客所有物', now_person='当前所有者',
                         next_person='下个所有者', device_available_status='设备物理状态', device_online_status='设备在线状态',
                         tips='备注', backup_1='备用字段 1', backup_2='备用字段 2', backup_3='备用字段 3',
                         create_time='创建时间', update_time='更新时间')

    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.username in ('ASDL1B1DL033', 'ASDL1B8DL002'):
                return True
            else:
                return False
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return flask.redirect(flask.url_for('main.auth_index'))


class UserModelViewAuth(ModelView):
    column_display_pk = True
    column_labels = dict(id='No.', username='用户名', password_hash='密码', name='昵称', backup_1='备用字段 1',
                         backup_2='备用字段 2', backup_3='备用字段 3', member_since='注册时间', last_seen='上次在线时间')

    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.username in ('ASDL1B1DL033', 'ASDL1B8DL002'):
                return True
            else:
                return False
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return flask.redirect(flask.url_for('main.auth_index'))


admin = Admin(name='数据库管理', index_view=AdminIndexView(), template_mode='bootstrap3')

admin.add_view(DeviceModelViewAuth(Device, db.session, name='设备表管理'))
admin.add_view(UserModelViewAuth(User, db.session, name='用户表管理'))

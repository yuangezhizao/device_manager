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
                         next_person='下个所有者', device_available_status='设备可用性状态', device_online_status='设备在线状态',
                         tips='备注', insert_time='插入时间', update_time='更新时间')

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
    column_labels = dict(id='No.', username='用户名', password_hash='密码哈希', name='昵称', member_since='注册时间',
                         last_seen='上次在线时间')

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

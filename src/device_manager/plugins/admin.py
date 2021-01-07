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
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return flask.redirect(flask.url_for('main.auth_index'))


class ModelViewAuth(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return flask.redirect(flask.url_for('main.auth_index'))


admin = Admin(name='数据库管理', index_view=AdminIndexViewAuth(), template_mode='bootstrap3')

admin.add_view(ModelViewAuth(Device, db.session))
admin.add_view(ModelViewAuth(User, db.session))

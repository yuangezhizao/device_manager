#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 20:51
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
import datetime

from flask_login import UserMixin

from device_manager.plugins.extensions import db


class User(db.Model, UserMixin):
    __bind_key__ = 'alsi'
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(50), unique=True)
    email = db.Column(db.VARCHAR(50), unique=True)
    password_hash = db.Column(db.VARCHAR(128))
    name = db.Column(db.VARCHAR(50))
    member_since = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return f'<User {self.username, self.name}>'

    def set_password(self, password):
        # from werkzeug.security import generate_password_hash
        # self.password_hash = generate_password_hash(password)
        self.password_hash = password

    def validate_password(self, password):
        # from werkzeug.security import check_password_hash
        # return check_password_hash(self.password_hash, password)
        from werkzeug.security import safe_str_cmp
        return safe_str_cmp(self.password_hash, password)

    def ping(self):
        self.last_seen = datetime.datetime.utcnow()
        db.session.commit()

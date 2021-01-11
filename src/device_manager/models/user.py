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
from sqlalchemy.sql import func

from device_manager.plugins.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    email = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    password_hash = db.Column(db.VARCHAR(128), nullable=False)
    name = db.Column(db.VARCHAR(50), nullable=False)
    backup_1 = db.Column(db.VARCHAR(255))  # 备用字段 1
    backup_2 = db.Column(db.VARCHAR(255))  # 备用字段 2
    backup_3 = db.Column(db.VARCHAR(255))  # 备用字段 3
    member_since = db.Column(db.DateTime(), server_default=func.now())
    last_seen = db.Column(db.DateTime(), server_default=func.now(), onupdate=func.now())

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

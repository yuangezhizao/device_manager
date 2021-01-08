#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:17
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
from device_manager.plugins.extensions import db


class Device(db.Model):
    __bind_key__ = 'alsi'
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.VARCHAR(50))  # 设备类型
    serial = db.Column(db.VARCHAR(50), nullable=False)  # 设备序列号
    customer = db.Column(db.VARCHAR(50), nullable=False)  # 客户所有物
    now_person_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 当前所有者
    now_person = db.relationship('User', foreign_keys=[now_person_id])

    next_person_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 下个所有者
    next_person = db.relationship('User', foreign_keys=[next_person_id])

    # TODO：所有者存储是否足够
    person_status = db.Column(db.Integer, default=0)  # 所有者状态
    device_status = db.Column(db.Integer, default=0)  # 设备状态
    # TODO：关联表
    tips = db.Column(db.VARCHAR(255))  # 备注
    insert_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

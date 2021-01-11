#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:17
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
from sqlalchemy.sql import func

from device_manager.plugins.extensions import db


class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.VARCHAR(50), nullable=False)  # 设备类型
    serial = db.Column(db.VARCHAR(50), nullable=False)  # 设备序列号
    license = db.Column(db.VARCHAR(50), nullable=False)  # 设备授权
    can_count = db.Column(db.Integer, nullable=False)  # CAN 通道数量
    lin_count = db.Column(db.Integer, nullable=False)  # LIN 通道数量
    customer = db.Column(db.VARCHAR(50), nullable=False)  # 客户所有物
    now_person_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 当前所有者
    now_person = db.relationship('User', foreign_keys=[now_person_id])

    next_person_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 下个所有者
    next_person = db.relationship('User', foreign_keys=[next_person_id])

    # TODO：所有者存储是否足够
    device_available_status = db.Column(db.Integer, default=0)  # 设备物理状态：0，设备完好；1，设备损坏；2，设备返还日本侧；3，设备借出
    device_online_status = db.Column(db.Integer, default=0)  # 设备在线状态：0，设备状态未上报；1，设备正在使用中；2，设备已停止使用
    # TODO：关联表
    tips = db.Column(db.VARCHAR(255))  # 备注
    backup_1 = db.Column(db.VARCHAR(255))  # 备用字段 1
    backup_2 = db.Column(db.VARCHAR(255))  # 备用字段 2
    backup_3 = db.Column(db.VARCHAR(255))  # 备用字段 3
    create_time = db.Column(db.DateTime, server_default=func.now())
    update_time = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:10
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
import flask

from device_manager.models.device import Device

app = flask.current_app
bp = flask.Blueprint('main', __name__)


@bp.route('/')
def site_index():
    return flask.render_template('index.html')


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

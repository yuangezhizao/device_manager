#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:10
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
import flask

app = flask.current_app
bp = flask.Blueprint('main', __name__)


@bp.route('/')
def site_index():
    return 'index'

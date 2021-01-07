#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:09
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""


def register_views(flask_app):
    """ Register the blueprints using the flask_app object """
    from device_manager.views import (
        main,
    )
    flask_app.register_blueprint(main.bp)

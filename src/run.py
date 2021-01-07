#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:12
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
from device_manager import create_app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=5000, threaded=True)

#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2019/10/16 0016 0:35
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
"""
# activate_this = "C:\\Users\\Administrator\\.virtualenvs\\LAB-QaV1et56\\Scripts\\activate_this.py"
# with open(activate_this) as file_:
#    exec(file_.read(), dict(__file__=activate_this))

import logging
import sys

logging.basicConfig(stream=sys.stderr)

# Expand Python classes path with your app's path
sys.path.insert(0, 'D:\Apache24\htdocs\device_manager')

from run import create_app

app = create_app('production')

# Put logging code (and imports) here ...

# Initialize WSGI app object
application = app

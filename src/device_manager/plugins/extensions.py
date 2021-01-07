#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/1/7 10:17
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020~2021 yuangezhizao <root@yuangezhizao.cn>
"""
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
compress = Compress()

# device_manager

设备管理系统

## 背景

部门内所使用的 Vector 设备随着社内业务量的增加，利用率也在不断升高，设备在人员之间的交换一直是线下操作。 为了定位到某一设备具体在谁的名下，以及查询设备是否正在使用中，开发此系统以解决上述问题

### 一、设备转移：

1. A 用户将自己名下的 1 设备借出给 B，需登录此系统将 1 设备的下一所有者设为 B
2. B 用户登录此系统确认接收 1 设备，此时 1 设备的当期所有者即为 B，下一所有者清空

### 二、设备状态：

1. 部门全员电脑设定计划任务运行某脚本，脚本尝试获取 USB 设备的序列号并发送至服务端，服务端更新对应序列号设备的“上次在线时间”为当前时间
2. 根据当前时间距离“上次在线时间”的时间差来判断在线状态：小于 20min 则在线，大于 20min 则离线

## 技术栈

1. 前端：Jinja2 + Fomantic-UI
2. 后端：Flask
3. 数据库：SQLite

## 安装

``` shell
pip3 install -r requirements.txt
```

## 依赖

```shell
Flask
Flask-Login
Flask-SQLAlchemy
Flask-Admin
Flask-Mail
Flask-Migrate
Flask-Moment
python-dotenv
Flask-BabelEX
```

## `Agent`打包

```shell
pyinstaller -F device_manager_report.py --nowindowed --noconsole
```

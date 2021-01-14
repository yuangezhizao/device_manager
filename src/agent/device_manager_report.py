import getpass
import socket

import clr
import requests

clr.AddReference('vxlapi_NET')

from vxlapi_NET import *

myDriver = XLDriver()
myDriverConfig = XLClass.xl_driver_config()


def get_serial():
    myStatus = myDriver.XL_OpenDriver()

    if (myStatus != XLDefine.XL_Status.XL_SUCCESS):  # 0 means XL_SUCCESS
        print('ERROR XL_OpenDriver')
        return 0

    myStatus, ref = myDriver.XL_GetDriverConfig(myDriverConfig)

    print(f'dllVersion：{myDriverConfig.dllVersion}')

    if (myStatus != XLDefine.XL_Status.XL_SUCCESS):
        print('ERROR XL_GetDriverConfig')
        return 0

    # 55:vn1610, 57:vn1630, 63:vn1611 81：vn7610,
    for i in range(myDriverConfig.channelCount):
        serial = myDriverConfig.channel[i].serialNumber
        print(f'serial：{serial}')
        if (myDriverConfig.channel[i].transceiverName.find('Virtual CAN') == -1):
            # print(myDriverConfig.channel[i].hwType)
            serial = myDriverConfig.channel[i].serialNumber
            return serial
        else:
            return 0


def get_vtest_studio_serial():
    # TBD
    pass


def report():
    import platform
    serial = get_serial()
    if serial == 0:
        serial = get_vtest_studio_serial()
    hostname = socket.gethostname()
    user = getpass.getuser()
    platform = platform.platform()
    return requests.get(
        f'http://10.30.10.216:5000/report?serial={serial}&hostname={hostname}&user={user}&platform={platform}&version=100').text


if __name__ == '__main__':
    try:
        print(report())
    except Exception as e:
        print(e)

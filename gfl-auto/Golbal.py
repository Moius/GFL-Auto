# -*- encoding=utf8 -*-

from airtest.core.api import *

device_info = input("请输入你要链接的地址，如不清楚则留空：")
if device_info :
    device_info = "andriod"
else:
    device_info = "127.0.0.1"
print(device_info)
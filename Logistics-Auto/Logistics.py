# -*- encoding=utf8 -*-

__author__ = "ELXIAGHT"
# TODO: 控制台的外置core模块，使用控制台输入对应参数
from airtest.core.api import *
from airtest.cli.parser import cli_setup
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android:///127.0.0.1:5555?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"])
import logging
import datetime
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

count = 0
k = 0

# 获取时间函数
def get_time():
	times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return times

# 检查出征状态,检测到后勤自动输出对应变量.
def Excute():
    
    global k
    global count
    
    isexists1= exists(Template(r"Logistics-Auto\img\start_all.png",record_pos=(-0.339, -0.077), resolution=(1600, 900)))
    if isexists1:
        k=1
        touch(isexists1)
        sleep(1)
        isexists2 = exists(Template(r"Logistics-Auto\img\confirm.png",record_pos=(0.001, -0.039), resolution=(1600, 900)))
        if isexists2:
            touch(isexists2)
        times = get_time()
        print("执行成功，当前时间>>"+times)  
        count = count + 1             
    else:
        k=0
        
#main 主函数
while True:
    if k==0:
        times = get_time()
        print("当前时间>>"+times)
        Excute()
    else:
        k=0
        print("成功收取次数>>"+str(count))
        sleep(300) #如果每次后勤最短间隔时间为其他时间请改为其他时间 eg:间隔时间为2分钟请改为120.
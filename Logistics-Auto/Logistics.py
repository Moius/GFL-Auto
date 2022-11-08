# -*- encoding=utf8 -*-
__author__ = "mobius"

from airtest.core.api import *

auto_setup(__file__)
import logging
import datetime
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

count = 0
k = 0
n = 0

# 获取时间函数

def get_time():
	times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return times

# 检查函数,检测到后勤自动输出对应变量.

def Check():
    
    global k
    isexists1= exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
    if isexists1:
        k=1
        Excute()                
    else:
        k=0
# 执行函数,判断成功时的执行脚本.

def Excute():
    
    global count
    global n
    
    touch(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
    sleep(3)
    isexists2 = exists(Template(r"tpl1612894445416.png",record_pos=(0.001, -0.039), resolution=(1440, 810)))
    sleep(1)
    if isexists2:
        touch(Template(r"tpl1612894456578.png", record_pos=(0.082, 0.105), resolution=(1440, 810)))
        
    times = get_time()
    print("执行成功，当前时间>>"+times)
    n = 1
    count = count + 1
        
#main 主函数

while True:
    if k==0 and n==0:
        times = get_time()
        print("校准中，当前时间>>"+times)
        Check()
        sleep(30) #校准后整个循环的等待时间,可以稍微大一点 不建议超过一分钟(60).
    elif k==1:
        Check()
        sleep(10) #执行完一次动作后的等待时间,看反应速度,一般10s足够跳出下一个后勤成功了.不建议少于5s.
    else:
        n=0
        print("成功收取后勤次数>>"+str(count))
        sleep(3600) #如果每次后勤最短间隔时间为其他时间请改为其他时间 eg:间隔时间为2分钟请改为120.
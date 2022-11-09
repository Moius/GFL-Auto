# -*- encoding=utf8 -*-
# GFL_Core 
from airtest.core.api import *
import datetime

def get_time():
	times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return times
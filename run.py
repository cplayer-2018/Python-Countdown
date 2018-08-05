# -*- coding: utf-8 -*-
# 2018-8-5 11:30:15
import time,easygui as eg

s = 1800
Event = input('事件名 > ')
for i in range(1800):
	s = s - 1
	print('事件',Event,'，剩余',s,'秒。')
	time.sleep(1)
eg.msgbox(('事件',Event,'，30 分钟倒计时结束。'), '倒计时提醒', '好的')

""" Lite
for i in range(1799):
	time.sleep(1)
eg.msgbox('倒计时结束。')
"""

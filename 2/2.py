#!/usr/bin/env python
# -*- codeing : utf-8 -*-

'''
作者：洛南雪
地点：地球村-北京
'''
import turtle
import math
import sys
l = 800
n = input("要画几边形?\n")
try:
    n = int(n)
except:
    print("他妈的,输入正常一点好吗？")
    sys.exit()
if n < 3:
    print("他妈的，你有本事你画个试试？")
    sys.exit()
f = math.sin(math.pi * (90/n) / 180)
l = l * f
t = turtle.Pen()
for x in range(n):
    t.forward(l)
    t.left(360/n)
t.right(180/n)
l = l / 2
t.circle(l / math.sin(math.pi * (180/n) / 180))


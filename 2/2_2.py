#!/usr/bin/env python
# -*- codeing : utf-8 -*-

import turtle
import math
import sys
l = 800
n = input("要画几边形?\n")
n = int(n)
if n < 3:
    print("他妈的，你有本时你画个一边行试试")
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
input()


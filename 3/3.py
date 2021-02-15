#!/usr/bin/env python
# -*- codeing : utf-8 -*-
import socket
import time
import sys

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",11223))
n = 0
while True:
    time.sleep(1)
    data = "1" * 1024
    client.send(data.encode())
    n = n + 1
    print(n)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#-------author@manik---------
from socket import *
host = ""
port = 4444
server_s = socket(AF_INET, SOCK_STREAM)
server_s.connect((host , port))

while true:
    message = raw_input("Message")
    server_s.send(message)
    print("Awaiting reply")
    reply = server_s.recv(1024)#max data that can be recieved
    print(" recieved" , repr(reply))

server_s.close()

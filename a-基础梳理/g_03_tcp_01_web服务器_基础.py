"""
@author: yrmt
@contact: butanoler@gmail.com
@file: g_03_tcp_01_web服务器_基础.py
@time: 2019/8/20
"""
import time
import socket

# # 下为抓包数据
# 请求：
"""
GET http://127.0.0.1/a HTTP/1.1
"""
# 返回：(不空行之前为header,首个空行之后为内容)
"""
HTTP/1.1 200 OK
Server: nginx/1.8.1
Date: Mon, 02 Sep 2019 08:59:57 GMT
Content-Type: application/text
Content-Length: 4
Connection: keep-alive

haha
"""


def deal_client(client_tcp, client_addr):
    rece = client_tcp.recv(1024).decode()
    rece_data = rece.split("\r\n")[0].split(" ")
    client_tcp.send("HTTP/1.1 200 OK\r\n\r\n{}-{}".format('hello', time.time()).encode())
    print(client_addr, rece_data)
    client_tcp.close()  # 处理完即关闭,正常情况下服务器不主动关闭


tcp_server = None
try:
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立tcp服务
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind(("", 8890))  # 绑定8890端口
    tcp_server.listen(124)
    while True:
        client_tcp, client_addr = tcp_server.accept()  # 持续阻塞监听tcp连接
        deal_client(client_tcp, client_addr)  # 处理
except KeyboardInterrupt:
    if tcp_server:
        tcp_server.close()

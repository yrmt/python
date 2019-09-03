"""
@author: yrmt
@contact: butanoler@gmail.com
@file: g_03_tcp_02_web服务器_轮询.py
@time: 2019/8/20
"""
import socket

client_tcps = []
tcp_server = None


def deal_client(client_tcp, client_addr):
    try:
        rece = client_tcp.recv(1024)
        if not rece:
            print("disconnect: {}".format(client_addr))
            client_tcp.close()
            client_tcps.remove((client_tcp, client_addr))
        else:
            rece_data = rece.decode().split("\r\n")[0].split(" ")
            client_tcp.send("HTTP/1.1 200 OK\r\ncontent-length: 5\r\n\r\n{}".format('hello').encode())
            print('receive from:{}->{}'.format(client_addr, rece_data))
    except BlockingIOError:
        pass


try:
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立tcp服务
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind(("", 8890))  # 绑定8890端口
    tcp_server.listen(124)
    tcp_server.setblocking(False)  # !!!设置非阻塞模式
    while True:
        try:
            client_tcp, client_addr = tcp_server.accept()  # 持续阻塞监听tcp连接
            client_tcp.setblocking(False)  # !!!设置非阻塞模式
        except BlockingIOError:
            pass
        else:
            print("connect: {}".format(client_addr))
            client_tcps.append((client_tcp, client_addr))
        for (client_tcp, client_addr) in client_tcps:  # ！！！耗资源轮询！！！
            deal_client(client_tcp, client_addr)  # 处理请求
except KeyboardInterrupt:
    if tcp_server:
        tcp_server.close()
    for client_tcp in client_tcps:
        client_tcp[0].close()

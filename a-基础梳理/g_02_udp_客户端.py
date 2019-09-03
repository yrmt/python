"""
@author: yrmt
@contact: butanoler@gmail.com
@file: g_02_udp_客户端.py
@time: 2019/8/20
"""
import socket

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字
udp_client.bind(('', 10001))  # 绑定端口,不写给随机端口
udp_client.sendto('你好'.encode(), ('127.0.0.1', 10000))
udp_client.close()

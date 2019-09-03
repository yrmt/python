"""
@author: yrmt
@contact: butanoler@gmail.com
@file: g_01_udp_服务端.py
@time: 2019/8/20
"""
import socket

# socket起源于Unix，而Unix/Linux基本哲学之一就是“一切皆文件”，都可以用“打开open –> 读写write/read –> 关闭close”模式来操作。
# Socket就是文件模式的一个实现，socket即是一种特殊的文件 (参数2+ip地址+端口号实例一个socket) 一些socket函数就是对其进行的操作（读/写IO、打开、关闭）

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字
# 参数1：
# AF_INET，指定so_pcb中的地址要采用ipv4地址类型
# AF_INET6，指定so_pcb中的地址要采用ipv6的地址类型
# AF_LOCAL/AF_UNIX，指定so_pcb中的地址要使用绝对路径名
# 参数2：
# SOCK_STREAM 提供有序的、可靠的、双向的和基于连接的字节流服务，当使用Internet地址族时使用TCP。
# SOCK_DGRAM 支持无连接的、不可靠的和使用固定大小（通常很小）缓冲区的数据报服务，当使用Internet地址族使用UDP。
# SOCK_RAW 原始套接字，允许对底层协议如IP或ICMP进行直接访问，可以用于自定义协议的开发。

udp_server.bind(('', 10000))  # ip绑定,端口绑定,
(msg, addr) = udp_server.recvfrom(1024)
print(msg.decode())
print(addr)
udp_server.close()

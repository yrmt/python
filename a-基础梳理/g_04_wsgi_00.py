"""
@author: yrmt
@contact: butanoler@gmail.com
@file: g_04_wsgi_00.py
@time: 2019/9/2
"""


# Web Server Gateway Interface ->  Web 服务器网关接口
# https://www.python.org/dev/peps/pep-3333/

# 嵌入wsgi后 只用实现一个方法
# eg:application
# 入参1: environ 是一个字典对象，包含CGI风格的环境变量。此对象必须是内置的Python字典（不是子类，UserDict或其他字典模拟）
# 并且允许应用程序以其期望的任何方式修改字典。字典还必须包括某些WSGI所需的变量（在后面的部分中描述），并且还可以包括服务器特定的扩展变量，根据将在下面描述的约定命名。


# def application(environ, start_response):
# start_response('200 OK', [('Content-Type', 'text/html')])
# return '<h1>Hello, web!</h1>'

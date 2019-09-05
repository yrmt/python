"""
@author: yrmt
@contact: butanoler@gmail.com
@file: g_04_wsgi_01.py
@time: 2019/9/2
"""
import select
import socket


class WSGIServer(object):
    def __init__(self, app, port=8890):
        self.app = app
        self.port = port
        self.client_tcps = {}  # 存放客户端tcp连接
        self.running = False
        self.epl = select.epoll()  # 实例化 epoll
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_server.bind(("", self.port))
        self.tcp_server.listen(124)
        self.epl.register(self.tcp_server.fileno(), eventmask=select.EPOLLIN)
        print("server init ")

    def __enter__(self):
        print("server run {}".format(self.port))
        self.running = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("server exit")
        self.running = False
        tcp_file_no = self.tcp_server.fileno()
        for fileno, (client_tcp, client_addr) in self.client_tcps.items():
            self.epl.unregister(fileno)
            client_tcp.close()
            print("service disconnect:{}".format(client_addr))
        self.client_tcps.clear()
        self.epl.unregister(tcp_file_no)
        self.tcp_server.close()

    def deal(self):
        while self.running:
            fd_event_list = self.epl.poll()  # 堵塞
            for fd, event in fd_event_list:
                if fd == self.tcp_server.fileno():  # 主tcp
                    newtcp, client_addr = self.tcp_server.accept()
                    print("connect:{},fileno:{}".format(client_addr, newtcp.fileno()))
                    self.epl.register(newtcp.fileno(), select.EPOLLIN)
                    self.client_tcps[newtcp.fileno()] = (newtcp, client_addr)
                elif select.EPOLLIN == event:
                    newtcp, client_addr = self.client_tcps.get(fd)
                    rece = newtcp.recv(1024)
                    if rece:
                        rece_data = rece.decode().split("\r\n")[0].split(" ")
                        print('receive from:{}->{}'.format(client_addr, rece_data))
                        body = self.app({"path": rece_data[1]}, self.start_response)
                        res_status = "HTTP/1.1 {}".format(self.status)
                        res_header = "\r\n".join(["{}:{}".format(head[0], head[1]) for head in self.headers])
                        res = "{}\r\n{}\r\n\r\n{}".format(res_status, res_header, body)
                        newtcp.send(res.encode())
                    else:
                        print("disconnect:{}".format(client_addr))
                        self.epl.unregister(fd)
                        newtcp.close()
                        self.client_tcps.pop(fd)

    def start_response(self, status, headers):
        self.status = status
        self.headers = headers
        self.headers.append(("Server", "butanoler"))


def application(env, start_response):
    def index():
        return "index2.aaaa"

    def index2():
        return "index2.2222"

    def notfound():
        return "404"

    if env.get("path") == "/a":  # 可用装饰器实现 -> flask
        res = index()
    elif env.get("path") == "/b":
        res = index2()
    else:
        res = notfound()
    start_response("200 OK", [("Content-Type", "text\html"), ("Content-Length", len(res))])
    return res


if __name__ == '__main__':
    # linux下运行
    with WSGIServer(application, 8890) as app:
        try:
            app.deal()
        except KeyboardInterrupt:
            pass

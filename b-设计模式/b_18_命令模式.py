class Mail(object):
    # 执行器
    def __init__(self):
        self._sender = None

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, _sender):
        self._sender = _sender

    def exe(self):
        print("执行器执行命令")
        self._sender.action()


class Gmail(object):
    # 执行
    def action(self):
        print("Gmail action")


class Person(object):
    # 命令发出者
    def __init__(self):
        self._mail = None

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, _mail):
        print("人绑定发送方式")
        self._mail = _mail

    def action(self):
        print("人发出指令")
        self._mail.exe()


if __name__ == '__main__':
    m = Mail()
    m.sender = Gmail()
    p = Person()
    p.mail = m
    p.action()

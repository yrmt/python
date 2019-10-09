"""
装饰器模式 Python 使用注解
"""


class Mail(object):
    def send(self):
        print("send mail")


class MailProxy(object):
    def __init__(self):
        self.sender = Mail()

    def send(self):
        print("start send")
        self.sender.send()
        print("end send")


if __name__ == '__main__':
    mp = MailProxy()
    mp.send()

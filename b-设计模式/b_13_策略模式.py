import abc


class Helper(object):
    def create_mail(self):
        print("Helper create_help")


class SendInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send_mail(self):
        pass


class Gmail(SendInterface, Helper):
    def send_mail(self):
        self.create_mail()
        print("Gmail send mail")


class QQmail(SendInterface, Helper):
    def send_mail(self):
        self.create_mail()
        print("Gmail send mail")


if __name__ == '__main__':
    qm = QQmail()
    qm.send_mail()
    print("*" * 30)
    gm = Gmail()
    gm.send_mail()

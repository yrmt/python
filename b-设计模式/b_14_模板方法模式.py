import abc


class Send(metaclass=abc.ABCMeta):
    def send(self):
        mail = self.creat_mail()
        print("send mail ", mail)

    @abc.abstractmethod
    def creat_mail(self):
        pass


class Gmail(Send):
    def creat_mail(self):
        return "this is gmail send"


if __name__ == '__main__':
    gm = Gmail()
    gm.send()

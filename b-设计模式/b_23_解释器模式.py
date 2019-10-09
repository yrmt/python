class GMail(object):
    def send(self, dic: dict):
        print("GMail", dic.get("head"), dic.get("body"))


class QMail(object):
    def send(self, dic: dict):
        print("QMail", dic.get("head"), dic.get("body"))


if __name__ == '__main__':
    QMail().send({"head": 'this is header', 'body': 'this is body'})
    GMail().send({"head": 'this is header', 'body': 'this is body'})

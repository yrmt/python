import abc


class JdbcBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        pass


class OracleJdbc(JdbcBase):
    def connect(self):
        print("OracleJdbc connect")


class MysqlJdbc(JdbcBase):
    def connect(self):
        print("MysqlJdbc connect")


class Jdbc(object):
    def __init__(self, connection):
        self.connection = connection

    def connect(self):
        self.connection.connect()


if __name__ == '__main__':
    j = Jdbc(OracleJdbc())
    j.connect()

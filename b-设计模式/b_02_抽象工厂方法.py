# 适用场景，优点：
# 1. 解决工厂模式需要频繁更新工厂
import abc


class ClientFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("{} client __exit__".format(self.__name__))
        self.close()


class RemoteClient(metaclass=abc.ABCMeta, ClientFactory):
    @abc.abstractmethod
    def exec_command(self, command):
        pass


class SftpClient(RemoteClient):

    def connect(self):
        print("sftp connect")

    def close(self):
        print("sftp close")

    def exec_command(self, command):
        print("sftp :{}".format(command))


class SshClient(RemoteClient):
    def connect(self):
        print("ssh connect")

    def close(self):
        print("ssh close")

    def exec_command(self, command):
        print("ssh :{}".format(command))


if __name__ == '__main__':
    with SshClient() as client:
        client.exec_command("rm -rf /")

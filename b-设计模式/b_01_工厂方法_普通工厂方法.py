# 适用场景，优点：
# 1. 大量产品需要创建，具有相同接口。
# 2. 工厂管理对象的创建，使用者不必知道创建过程，减少因创建逻辑导致的错误。
# 缺点：
# 1. 类的创建依赖工厂类，扩展程序需要对工厂修改。违背开闭原则。
import abc


class RemoteClient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

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


class ClientFactory(object):
    def __init__(self, client_type):
        self.client_type = client_type

    def __enter__(self):
        print("{} client __enter__".format(self.client_type))
        if self.client_type == 'sftp':
            self._client = SftpClient()
        elif self.client_type == 'ssh':
            self._client = SshClient()
        else:
            raise Exception("无效的 client_type")
        self._client.connect()
        return self._client

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("{} client __exit__".format(self.client_type))
        self._client.close()


if __name__ == '__main__':
    with ClientFactory("ssh") as client:
        client.exec_command("rm -rf /")

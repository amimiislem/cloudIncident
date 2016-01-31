import paramiko


def get_sftp():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.49.130', username='root', password='123456')
    return client

def test2():
    client = get_sftp()
    sftp = client.open_sftp()
    filepath = '/home/hello.txt'
    localpath = '/home/islem/Public/OpenStack/ssh.properties'
    sftp.put(localpath, filepath)
    sftp.stat('/tmp')
    sftp.close()


if __name__ == "__main__":
    test2()
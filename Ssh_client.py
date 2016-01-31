import paramiko as paramiko

__author__ = 'islem'


class ssh_client:
    def __init__(self,ip, user='root', passwd=''):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, username=user, password=passwd)


    def exec_cmd(self, cmd='uname'):
        return self.ssh.exec_command(cmd)

    def ssh_close(self):
        self.ssh.close()

    def send_file(self,localpath,filepath):
        sftp = self.ssh.open_sftp()
        sftp.put(localpath, filepath)
        sftp.close()
    def get_file(self,localpath,filepath):
        sftp = self.ssh.open_sftp()
        sftp.get(localpath, filepath)
        sftp.close()

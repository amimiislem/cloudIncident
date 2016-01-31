import paramiko
  
class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return
  
client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect('192.168.49.130', username='root',password='123456')  # password='')
  
channel = client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

stdin.write('echo $PATH\recho Hello, world\rexit\r')
#stdin.write("$x = 'hellox'")
print(stdout.read())
  
client.close()
from Cloud_client import Cloud_client
from Config_Data import Config_data
from Ssh_client import ssh_client
from vm_service import vm_service
from Hypervisor_service import hypervisor_service

__author__ = 'islem'

def main():
    x = Cloud_client()
    vms = vm_service(x.get_client())
    hyp = hypervisor_service(x.get_client())
    print(vms.getvms)
    for vm in vms.getvms:
        #vm.unpause()
        print(getattr(vm, 'name'))
        print(getattr(vm, 'id'))
        print(getattr(vm, 'OS-EXT-SRV-ATTR:instance_name'))
        print('hyp type = ' + getattr(hyp.getvmhypervisorinfo(vm), 'hypervisor_type'))
        print('hyp name = '+getattr(hyp.getvmhypervisorinfo(vm), 'hypervisor_hostname'))
        #print('vcpu  = '+getattr(hyp.getvmhypervisorinfo(vm), 'hypervisor_version'))
        sshclient = ssh_client('192.168.49.130', passwd='123456')
        ssh_stdin, ssh_stdout, ssh_stderr = sshclient.exec_cmd('uname -a')
        print(ssh_stdout.readlines())
def test_config_data():
    server_conf = Config_data()
    data = server_conf.get_hyp_config('xenserver')
    print(data['IP'])
    print(data['PASS'])
    data2 = server_conf.get_cloud_config('Project_Name')
    print(data2['AUTH_URI'])

def test_hyp_cmd():
    config = Config_data()
    x = Cloud_client()
    vms = vm_service(x.get_client())
    hyper_service = hypervisor_service(x.get_client())
    hyp = hyper_service.getvmhypervisorinfo(vms.getvms[0])
    print(hyper_service.get_hyp_name(hyp))
    hyp_config = config.get_hyp_config(hyper_service.get_hyp_name(hyp))
    ssh = ssh_client(ip=hyp_config['IP'], passwd=hyp_config['PASS'])
    print(hyp_config['LOCAL_SCRIPT'])
    ssh.send_file(hyp_config['LOCAL_SCRIPT'],hyp_config['LOCAL_SCRIPT'])
    data = hyper_service.get_hyp_cmd(hyp)
    vm_hyp_name = vms.get_vm_hyp_name(vms.getvms[0])
    d = ''
    output = ''
    for key in data:
        cmd = data[key].replace('[script]',hyp_config['LOCAL_SCRIPT']).replace('[vm_name]',vm_hyp_name)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_cmd(cmd=cmd)
        output = str(ssh_stdout.readlines())[3:-4]
    if(output <> '' ):
        getsnapshot(ssh=ssh,filename=output)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_cmd(cmd="rm -f *.xva xen_snap.sh")
    ssh.ssh_close()

def getsnapshot(ssh,filename):
    ssh.get_file(localpath=filename,filepath='snapshot/'+filename)

if __name__ == '__main__':
    #main2()
    #test_config_data()
    test_hyp_cmd()
    #hyp()
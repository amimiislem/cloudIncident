import ConfigParser
import libvirt
__author__ = 'PC-ASUS'

class hypervisor_service:

    def __init__(self, novaClient):
        self.novaClient = novaClient

    def getvmhypervisorinfo(self, vm):
        #ip,type,
        hyp_hostname = getattr(vm, 'OS-EXT-SRV-ATTR:hypervisor_hostname')
        hyps = self.novaClient.hypervisors.list()
        for h in hyps:
            if h.hypervisor_hostname == hyp_hostname:
                return self.novaClient.hypervisors.get(h)
    def get_hyp_cmd(self,hypervisor):
        config = ConfigParser.RawConfigParser()
        config.read(filenames='ssh.properties')
        data = dict()
        i = 1
        while i>0 :
            try:
                data[i]=config.get(getattr(hypervisor,'hypervisor_type'), str(i))
            except ConfigParser.NoOptionError:
                i=-1
            i=i+1
        return data
    def get_hyp_name(self,hypervisor):
        return  getattr(hypervisor,'hypervisor_type')
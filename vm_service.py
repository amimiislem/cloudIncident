__author__ = 'PC-ASUS'
class vm_service:
    def __init__(self, client):
        self.client = client
    @property
    def getvms(self):
        return self.client.servers.list(detailed=True, search_opts={'all_tenants': 1})
    def get_vm_hyp_name(self,vm):
        return getattr(vm, 'OS-EXT-SRV-ATTR:instance_name')
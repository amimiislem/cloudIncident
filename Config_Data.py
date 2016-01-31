__author__ = 'root'
import ConfigParser

class Config_data:
    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read(filenames='auth.properties')
        self.config_hyp = ConfigParser.RawConfigParser()
        self.config_hyp.read(filenames='ssh.properties')

    def get_cloud_config(self,tenantName):
        data = dict()
        data['TYPE'] = self.config.get(tenantName, 'TYPE')
        data['AUTH_URI'] = self.config.get(tenantName, 'AUTH_URI')
        data['USERNAME'] = self.config.get(tenantName, 'USERNAME')
        data['PASSWORD'] = self.config.get(tenantName, 'PASSWORD')
        data['PROJECT_ID'] = self.config.get(tenantName, 'PROJECT_ID')
        return data
    def get_hyp_config(self,server_name):
        data = dict()
        data['IP'] = self.config_hyp.get(server_name, 'IP')
        data['PASS'] = self.config_hyp.get(server_name, 'PASS')
        data['LOCAL_SCRIPT'] = self.config_hyp.get(server_name, 'LOCAL_SCRIPT')
        return data
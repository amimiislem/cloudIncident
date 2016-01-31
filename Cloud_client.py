from keystoneclient.auth.identity import v2
from keystoneclient import session
from novaclient import client

import ConfigParser
from Config_Data import Config_data

__author__ = 'islem'

class Cloud_client:

    tenantName = 'Project_Name'

    def __init__(self):
        server_conf = Config_data()
        self.data = server_conf.get_cloud_config('Project_Name')
        self.client_type = self.data['TYPE']

    def get_nova_client(self):
        auth = v2.Password(auth_url=self.data['AUTH_URI'],
                           username=self.data['USERNAME'],
                           password=self.data['PASSWORD'],
                           tenant_name=self.data['PROJECT_ID'])
        sess = session.Session(auth=auth)
        return client.Client(2, session=sess)
    def get_client(self):
        if self.client_type == 'openstack':
            return self.get_nova_client()
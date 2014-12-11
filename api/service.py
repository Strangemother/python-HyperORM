
'''
The setup file helps define an initial build
and setup checks.
'''
import hyperdex
from hyperdex import admin, client
from hyperdex.client import HyperDexClientException

class HyperdexService(object):

    space_name = 'api_space'
    app_name = 'installer'

    def __init__(self, ip='127.0.0.1', port=1982):
        self.ip = ip
        self.port = port
        self.admin = None
        self.client = None

    def connect_admin(self, ip=None, port=None):
        '''
        create and connect a new hyperdex client.
        '''
        ip = self.ip if ip is None else ip
        port = self.port if port is None else port

        a = admin.Admin(ip, port)
        self.admin = a
        return a

    def connect_client(self, ip=None, port=None):
        '''
        Connect a new hyperdex client
        '''
        ip = self.ip if ip is None else ip
        port = self.port if port is None else port

        c = client.Client(ip, port)
        self.client = c
        return c

    def get_admin(self):
        '''
        Get or create a service admin
        '''
        if self.admin is None:
            return self.connect_admin()
        return self.admin

    def get_client(self):
        '''
        Get or creat a service client
        '''
        if self.client is None:
            return self.connect_client()
        return self.client

    def install_space(self):
        '''
        Install the service space. returns boolean if add_space ran correctly.
        '''
        space_str = '''
          space %(api_space)s
          key app_name
          attributes
            string keyname,
            string value,
            int timestamp
          subspace keyname
          tolerate 2 failures
        ''' % { 'api_space': self.space_name }
          # create 8 partitions

        print 'Installing:'
        print space_str
        print '------'

        admin = self.get_admin()
        added = admin.add_space(space_str)
        if added:
            client = self.get_client()
            # put a record
            putted = client.put(self.space_name, self.app_name, { 'value': 'installed'})
            return putted
        return added

    def installed(self):
        '''
        Returns boolean if the api is ready based upon a key within a
        required space.
        '''
        # hyperdex list-spaces
        client = self.get_client()

        try:
            ino = client.get( self.space_name, self.app_name )
            if ino is None:
                return False
            if ino['value'] is None:
                # corrupt install
                return False
            elif ino['value'] == 'installed':
                return True
            raise Exception('Installer did not expect %' % ino['value'])
            return False
        except HyperDexClientException as e:
            return False

    def install(self):
        ''' install the initial hyperdex tools'''
        if self.installed() is not True:
            return self.install_space()
        return self.installed()

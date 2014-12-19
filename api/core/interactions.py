import subprocess
import exceptions
from exceptions import ERR


class Interation(object):
    pass


class ProcessMixin(Interation):

    def cmd_process(self, *args):
        cms = ['hyperdex'] + [x for x in args]
        p = subprocess.Popen(cms, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out


class GetMixin(Interation):

    def get(self, key):
        client = None

        if self.service:
            client = self.service.get_client()
            print client

        print 'get from cloud', key
        if client is not None:
            import pdb; pdb.set_trace()
            d = client.get(self.name, key)
        return d

class InstallMixin(Interation):

    def install(self):
        '''
        Install the attached item.
        A service is required on the root object.
        If admin rights are not provided.

        exceptions.HyperError(ERR.ADMIN_ACCESS_DENIED)

        will be raised.
        '''
        if self.installed() is False:
            a = self.service.get_admin()
            if a is not None:
                hdef = self.hyper_def()
                added = a.add_space(hdef)
                return added
            else:
                raise exceptions.HyperError(ERR.ADMIN_ACCESS_DENIED)
                return False
        else:
            return True
        return False

    def remove(self):

        if self.installed() is True:
            a = space.service.get_admin()
            if a is not None:
                hdef = space.hyper_def()
                removed = a.rm_space(hdef)
                return removed
            else:
                raise exceptions.HyperError(ERR.ADMIN_ACCESS_DENIED)
                return False
        else:
            return True
        return False

    def installed(self):
        '''
        Return boolean if this space is installed
        '''
        return self.exists()


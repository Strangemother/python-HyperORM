import subprocess
import exceptions
from exceptions import ERR
from hyperdex.client import HyperDexClientException

class Interaction(object):
    pass


class ProcessMixin(Interaction):

    def cmd_process(self, *args):
        cms = ['hyperdex'] + [x for x in args]
        p = subprocess.Popen(cms, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out


class PutMixin(Interaction):

    def put(self, model=None, *args, **kwargs):
        client = None

        if self.service:
            client = self.service.get_client()
            return client.put(self.name, model.key, model.get_def())


class GetMixin(Interaction):

    def get(self, key, raw=False):
        client = None

        if self.service:
            client = self.service.get_client()
        else:
            raise exceptions.MissingServiceError()

        print 'get', key, 'from', self.name

        if client is None:
            raise exceptions.MissingClientError()

        try:
            d = client.get(self.name, key)
        except Exception as e:
            if e.symbol() in dir(ERR):
                raise exceptions.HyperClientError(e.status(), e.message())
            else:
                raise e

        if raw is True:
            return d

        Model = self.get_model()
        model = Model(key=key, data=d, space=self)
        return model


class InstallMixin(Interaction):

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
        '''
        Remote the attached space from the hypderDex spaces.
        Return boolean for success
        '''
        if self.installed() is True:
            a = self.service.get_admin()
            if a is not None:
                hdef = self.hyper_def()
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

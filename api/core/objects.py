import subprocess
import exceptions
from exceptions import ERR


class InteractionMixin(object):
    pass


class ProcessMixin(InteractionMixin):

    def cmd_process(self, *args):
        cms = ['hyperdex'] + [x for x in args]
        p = subprocess.Popen(cms, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out


class PutMixin(InteractionMixin):

    def put(self, model, client=None, space=None, service=None, *args, **kwargs):
        space = space or self
        if service is None and hasattr(self, 'service'):
            service = self.service
        if service:
            client = client or service.get_client()
            return client.async_put(space.name, model.key, model.get_def()).wait()


class GetMixin(InteractionMixin):

    def get(self, key, client=None, service=None):
        if service is None and hasattr(self, 'service'):
            service = self.service

        if service:
            client = client or service.get_client()

        if client is not None:
            d = client.async_get(self.name, key).wait()
            Model = self.get_model()
            model = Model(key=key, data=d, space=self)
            return model


class InstallMixin(InteractionMixin):

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


class Objects(GetMixin, PutMixin):

    def __init__(self, service=None, space=None):
        self.service = service
        self.space = space

    def save(self, service=None):
        '''
        Objects can be saved to it's associated
        space. A model is provided with it's associated
        space though _space.
        '''
        if service is None and hasattr(self, 'service'):
            service = self.service

        if hasattr(self, 'space') is False:
            if hasattr(self, '_space'):
                space = self._space
            elif hasattr(self, '__space__'):
                space = self.__space__
        else:
            space = self.space

        if service is None and space is not None:
            service = space.service

        return self.put(model=self, space=space, service=service)

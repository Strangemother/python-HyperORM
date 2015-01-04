global HyperError
from collections import namedtuple

ErrorDefinitions = {
    'MISSING_KEY': 'Key field is not defined in model "%(model.__class__.__name__)s"',
    'ADMIN_ACCESS_DENIED': 'This task required admin privileges',
    'MISSING_SERVICE': 'The Service is required',
    'HYPERDEX_CLIENT_COORDFAIL': 'Client Coordination failure'
}


class Struct:

    def __init__(self, **entries):
        self.__dict__.update(entries)

ERR = Struct(**ErrorDefinitions)


class HyperError(Exception):
    code = -1
    message = 'Error'
    model = None

    def __init__(self, code=None, message=None, model=None):
        self.code = code if code is not None else self.__class__.code
        self.message = message  if message is not None else self.__class__.message
        self.model = model if model is not None else self.__class__.model

    def __str__(self):

        name = self.__class__.__name__

        c = self.code % {'model': self.model or {},
                         'code': self.code,
                         'message': self.message
                         }

        if self.message is not None:
            s = '%s(%s): %s' % (name, c, self.message)
            return repr(s)
        else:
            s = '%s: %s' % (name, self.code)
            return repr(s)


class MissingServiceError(HyperError):
    message = 'Service is None or not provided'


class HyperClientError(HyperError):
    pass

class MissingClientError(HyperClientError):
    message = 'A service Client is None or not provided'


global HyperError
from collections import namedtuple

ErrorDefinitions = {
    'MISSING_KEY': 'Key field is not defined in model "%(model.__class__.__name__)s"',
    'ADMIN_ACCESS_DENIED': 'This task required admin privileges'
}


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

ERR = Struct(**ErrorDefinitions)

class HyperError(Exception):

    def __init__(self, code, message=None, model=None):
        self.code = code
        self.message = message
        self.model = None

    def __str__(self):

        name = self.__class__.__name__

        c = self.code % { 'model': self.model,
            'code': self.code,
            'message': self.message
        }

        if self.message is not None:
            s = '%s(%s): %s' % (name, c, self.message)
            return repr(s)
        else:
            s = '%s: %s' % (name, self.code)
            return repr(s)

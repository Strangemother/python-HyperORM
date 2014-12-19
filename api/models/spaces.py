from models import *

import exceptions
from exceptions import ERR

__all__ = ['AllTypes', 'Phonebook', 'FriendList', 'UserLock']

class Space(object):

    '''
    The name of your space provided to HyperDex. If the name is none,
    the lower case form of the class is used.
    '''
    name = None

    '''
    Tolerate the amount of failures to this space. default is 0 (no failures or
        0 percent tolerant.). 2 is a good dev number.
    '''
    tolerate = 0

    '''
    How many partitions to provide the data to.
    '''
    partitions = 0

    '''
    The model to reference when building the attributes for the hyperdex
    definition
    '''
    model = Model

    '''
    The service endpoint to call to when performing all remote procedures.
    This object will store the hyperdex client or hyperdex admin connection
    for reference.
    '''
    service = None

    def get_fields(self):
        '''
        Return all applicable fields of this model. First get_def() fetches
        the object definition. This is flattened to a list with
        all fields populated with a valid name.

        By precedence, field.name then the class created name 'pk', is referenced.
        '''
        defin = self.model().get_def()
        fields= []
        for k in defin:
            field = defin[k]
            field.name = k if field.get_name() is None else field.get_name()
            fields.append(field)
        return fields

    def get_attributes(self):
        '''
        Concat all the fields into the attributes string used for a space entry
        '''
        fields = self.get_fields()
        attrs = []
        for field in fields:
            fdef = field.get_definition()
            attr_str = '%s' % (fdef)
            attrs.append(attr_str)
        return attrs

    def get_model(self):
        '''
        Returns the model from self.model
        '''
        return self.model

    def get_space_name(self):
        if self.name is not None:
            return self.name
        else:
            return str(self.__class__.__name__).lower()

    def hyper_def(self):
        '''
        Return a string valid for HyperDex Space creation. Each field is
        referenced and a model is instansiated to create a space string
        to define the model written to the Hyperdex cloud.

        Once created, the data can be referenced through the provided ORM.
        '''
        _Model = self.get_model()

        # New model is created, turning a entire model into a working entity.
        model = _Model()
        # Subspaces to build based upon the model
        subspaces = []
        index = []
        tolerate = self.tolerate if hasattr(self, 'tolerate') is True else 0
        partitions = self.partitions if hasattr(self, 'partitions') is True else 0
        # To be later added.
        authorization = False
        # List all all attributes, or even the referenced model flattended into
        # its string components and ready to apply as a space.
        attr_str = ',\n'.join(self.get_attributes())

        # Name of the space to create
        name = self.get_space_name()

        model_key_name = model.get_key_name()


        # Get the key field name from the Key() field.
        if model_key_name is not None:
            key = 'key %s' % model_key_name
        elif hasattr(self, 'key'):
            key = model.key
        else:
            # A missing model.Key() and no model.Meta.key_name
            raise exceptions.HyperError(ERR.MISSING_KEY)

        '''hyperspace :: hyperspace()
                : scanner(NULL)
                , error(NULL)
                , strings()
                , name(NULL)
                , key()
                , attributes()
                , subspaces()
                , indices()
                , tolerate(1)
                , partitions(64)
                , authorization(false)
            {
                memset(buffer, 0, 1024);
            }

        '''
        # first three lines
        hs = ['''space %(name)s\n%(key)s''']

        # Model as attributes
        if attr_str:
            hs.append('attributes')
            hs.append('%(attributes)s')

        # indexes to create
        if len(subspaces) > 0:
           hs.append('subspace %(subspaces)s')

        #if len(index) > 0:
        #   hs.append('index %(indices)s')

        if tolerate > 0:
           hs.append('tolerate %(tolerate)s failures')

        if partitions > 0:
           hs.append('create %(partitions)s partitions')

        if authorization is True:
           hs.append('with authorization ')

        s = '\n'.join(hs)
        s = s % {
            'name': name,
            'key': key,
            'attributes': attr_str,
            'subspaces': subspaces,
            'indices': index,
            'tolerate': tolerate,
            'partitions': partitions
        }
        return s

    def installed(self):
        '''
        Return boolean if this space is installed
        '''
        import pdb; pdb.set_trace()


class AllTypes(Space):
    name = 'alldatatypes'
    model = AllTypesModel


class Phonebook(Space):
    name = 'phonebook'
    model = PhoneBookModel
    partitions = 8
    tolerate = 2


class FriendList(Space):
    model = FriendListModel


class UserLock(Space):
    model = UserLockModel

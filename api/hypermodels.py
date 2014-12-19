class Model(object):
    '''
     A reprensation of a hypdex model for the process of space creation
     in a hyperdex.
    '''


class Field(object):
    ''' A field to apply to hyper space and a python repesenation of
     a hyperspace '''
    data_type = None
    definition = '%(data_type)s'

    def get_definition(self):
        return self.definition % { 'data_type': self.data_type }

    def __unicode__(self):
        '''
        >>> from hypermodels import *
        >>> s=HyperSet()
        >>> unicode(s)
        u'set(None)'
        '''
        return self.get_definition()

    def __str__(self):
        '''
        When used in a string, the repesenation of the field
        is made
        '''
        return self.get_definition()


class Str(Field):
    '''
     The basic datatype in HyperDex is a byte string.
     If you don't specify the type of an attribute when creating a space,
     it is automatically treated as an 8-bit bytestring.

     This means that you'll have to encode and decode
     unicode strings as appropriate

     string foo
    '''

    '''
    field type provided to the hyperspace space definition.
    '''
    data_type = 'string'


class Int(Field):
    '''
     HyperDex supports get and put operations on integers. In addition to
     these basic operations, HyperDex provides atomic operations to
     manipulate integers using basic math operations.

     int foo
    '''
    data_type ='int'


class Set(Field):
    '''
     HyperDex supports simple set assignment (using the put
     interface), adding and removing elements with set_add and
     set_remove, taking the union of a set with set_union and storing
     the intersection of a set with set_intersect.

     set(int) foo
    '''
    data_type = 'set'
    sub_type = None
    definition = '%(data_type)s(%(sub_type)s)'

    def get_definition(self):
        return self.definition % {
            'data_type': self.data_type,
            'sub_type': self.sub_type
            }


class Map(Set):

    data_type = 'map'
    sub_types = (None, None)
    definition = '%(data_type)s( %(sub_types)s )'

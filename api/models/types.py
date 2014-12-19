import inspect


class Type(object):
    ''' A field to apply to hyper space and a python repesenation of
     a hyperspace '''
    data_type = None
    definition = '%(data_type)s %(name)s'
    types = None

    def get_definition(self):
        return self.definition % { 'data_type': self.data_type }

    def get_name(self):
        return self.name


    def get_definition(self):
        ns = []
        try:
            for t in iter(self.types):
                if inspect.isclass( t ):
                    if hasattr(t, 'data_type'):
                        ns.append(t.data_type)
                    else:
                        ns.append(t.__name__)

            types = ', '.join(ns)
        except TypeError, e:
            if hasattr(self.types, 'data_type'):
                types = self.types.data_type
            elif hasattr(self.types, '__name__'):
                types = self.types.__name__
            else:
                types = 'undefined'

        return self.definition % {
            'data_type': self.data_type,
            'types': types,
            'name': self.get_name()
            }

    def __init__(self, name=None, index=False):
        self.index = index
        self.name = name

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

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.name)

class Key(Type):
    data_type ='key'


class Str(Type):
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


class Int(Type):
    '''
     HyperDex supports get and put operations on integers. In addition to
     these basic operations, HyperDex provides atomic operations to
     manipulate integers using basic math operations.

     int foo
    '''
    data_type ='int'


class Float(Type):
    '''
     HyperDex supports get and put operations on integers. In addition to
     these basic operations, HyperDex provides atomic operations to
     manipulate integers using basic math operations.

     float foo
    '''
    data_type ='float'


class SubType(Type):
    types = (None,)
    definition = '%(data_type)s(%(types)s) %(name)s'

    def __init__(self, types=None, name=None):
        self.types = types or self.types
        self.name = None

    def __repr__(self):

        return "<types.%s('%s', %s)>" % (self.__class__.__name__, self.name, self.types)

class Set(SubType):
    '''
     HyperDex supports simple set assignment (using the put
     interface), adding and removing elements with set_add and
     set_remove, taking the union of a set with set_union and storing
     the intersection of a set with set_intersect.

     set(int) foo
    '''
    data_type = 'set'


class List(SubType):
    data_type = 'list'


class Map(Set):

    data_type = 'map'


class Document(Type):

    data_type = 'document'


class Field(object):

    '''
     A reprensation of a hypdex model for the process of space creation
     in a hyperdex.
    '''

    '''
    The dataType defines a reference to the definition and space value.
    This should be a data types.*
    '''
    data_type = None

    def __init__(self, name=None):
        self.name = name

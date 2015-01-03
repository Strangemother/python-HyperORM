import inspect
import types
import exceptions
from exceptions import ERR
from objects import Objects


class BaseModel(object):
    key = types.Key(name='pk')

    def get_key_name(self):
        meta_name = None
        if hasattr(self, 'Meta'):
            meta_name = getattr(self.Meta, 'key_name', None)

        if meta_name is not None:
            return meta_name
        elif self.key is not None:
            return 'key' if hasattr(self.key, 'name') is False else self.key.name
        else:
            raise exceptions.HyperError(ERR.MISSING_KEY, model=self)
        return None

    def get_attrs(self):
        '''
        Find all key attrs
        '''
        ignore = BaseModel.__dict__.keys()
        fields = []
        classes = self.__class__.__mro__
        # rint classes
        for parent_class in iter(classes):
            # print 'class', parent_class
            keys = parent_class.__dict__.keys()
            ckeys = self.__class__.__dict__.keys()
            for model_field in keys:
                is_cls = inspect.isclass(getattr(parent_class, model_field))
                is_meta = model_field == 'Meta' and is_cls
                name = model_field
                if is_meta or model_field in ignore or model_field.startswith('__'):
                    continue
                if model_field in ckeys:
                    fields.append(name)

        for field in ignore:
            name = field
            if field in ignore or field.startswith('__'):
                continue
            ignore.append(name)
        return fields

    def get_def(self):
        attrs = self.get_attrs()
        obj = {}
        for attr in attrs:
            obj[attr] = getattr(self, attr)
        return obj

    def get_indices(self):
        fields = self.get_attrs()
        indices = []
        index = 'index'

        for field in fields:
            tf = getattr(self, field)
            if hasattr(tf, index) and getattr(tf, index) is True:
                indices.append(field)

        return indices

    def __str__(self):
        return "HyperModel: %s" % (self.__unicode__())

    def __unicode__(self):
        kn = self.get_key_name()
        pk = getattr(self, kn) if hasattr(self, kn) else None
        return "%s('%s')" % (self.__class__.__name__, pk )

    def __repr__(self):
        return "<HyperModel %s.%s>" % (self.__class__.__module__, self.__class__.__unicode__(self) )

class Model(BaseModel, Objects):

    def __init__(self, key=None, data=None, space=None, **kwargs):

        if key is not None:
            setattr(self, 'key', str(key))

        if data is not None:
            self.__dict__.update(**data)
        self.__dict__.update(**kwargs)

        if space is not None:
            self._space = space


class InstallModel(Model):

    keyname = types.Str(index=True)
    value = types.Str()
    timestamp = types.Int()

    class Meta:
        key_name = 'app_name'


class UserLockModel(Model):

    class Meta:
        key_name = 'username'


class DocumentModel(Model):
    profile = types.Document()

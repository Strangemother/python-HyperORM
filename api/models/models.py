import inspect
import types
import exceptions
from exceptions import ERR


class BaseModel(object):
    key = types.Key(name='pk')

    def get_key_name(self):
        meta_name = None
        if hasattr(self, 'Meta'):
            meta_name = getattr(self.Meta, 'key_name', None)

        if meta_name is not None:
            return meta_name
        elif self.key is not None:
            return self.key.name
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
            ## print 'class', parent_class
            keys = parent_class.__dict__.keys()
            for model_field in keys:
                is_cls = inspect.isclass( getattr(parent_class, model_field) )
                is_meta = model_field == 'Meta' and is_cls
                name = model_field
                if is_meta or model_field in ignore or model_field.startswith('__'):
                    continue
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
            obj[attr] = getattr(self.__class__, attr)
        return obj

    def get_indices(self):
        fields = self.get_attrs()
        indices = []
        index ='index'

        for field in fields:
            tf = getattr(self, field)
            if hasattr(tf, index) and getattr(tf, index) is True:
                indices.append(field)

        return indices


class Model(BaseModel):
    pass


class InstallModel(Model):
    app_name = types.Key()
    key_name = types.Str()
    value = types.Str()


class FriendListModel(Model):
    first = types.Str()
    last = types.Str()
    friends = types.Set(types.Str)

    class Meta:
        key_name = 'username'


class NamedInstallModel(InstallModel):
    ss = types.Set(types.Str)


class AllTypesModel(Model):
    s = types.Str()
    i = types.Int()
    f = types.Float()
    ls = types.List( types.Str )
    ss = types.Set(types.Str)
    mss = types.Map( (types.Str, types.Str, ) )
    msi = types.Map( (types.Str, types.Int, ) )


class PhoneBookModel(Model):
    first = types.Str(index=True)
    last = types.Str(index=True)
    phone = types.Int(index=True)


class UserLockModel(Model):

    class Meta:
        key_name = 'username'

class DocumentModel(Model):
    profile = types.Document()

from core.models import Model, InstallModel
from core import types


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


class AccountsModel(Model):
    name = types.Str()
    balance = types.Int()

    class Meta:
        key_name = 'account'

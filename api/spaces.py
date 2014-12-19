from core.spaces import Space, Process
from models import *


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

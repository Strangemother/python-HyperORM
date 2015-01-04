from ..api.service import Service
from ..api.spaces import Phonebook
import random


def phonebook():
    sv = Service()
    pb = Phonebook(sv)
    installed = pb.installed()

    if installed is False:
        print 'Install phonebook'
        installed = pb.install()

    if installed is False:
        print 'Could not install phonebook'

    return pb


def phonebook_put(key_name='bob'):
    pb = phonebook()
    if pb is None:
        return False

    return pb.service.client.put('phonebook', key_name, {
        'first': 'Robert',
        'last': 'Smith',
        'phone': 441415546654
    })


def phonebook_put_model(key_name='bob'):
    pb = phonebook()
    if pb is None:
        return False

    PhoneBookModel = pb.get_model()

    model = PhoneBookModel()
    model.key = key_name
    model.first = 'Edward'
    model.last = 'Holmes'
    model.phone = 234895779345

    saved = pb.put(model)
    print 'saved', model.key, saved


def phonebook_put_many(count=1000):
    import names

    saves = 0
    counter = 0
    pb = phonebook()
    if pb is None:
        return False

    PhoneBookModel = pb.get_model()

    while counter < count:
        name = names.get_full_name()
        f, l = name.split(' ')
        model = PhoneBookModel(name)
        model.first = str(f)
        model.last = str(l)
        model.phone = long(random.randrange(11111111, 99999999999))

        saved = pb.put(model)
        if saved:
            saves += 1
        counter += 1

from service import Service
from spaces import Phonebook


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
	pb = phonebook();
	if pb is None: return False

	return pb.service.client.put('phonebook', key_name, {
	    'first': 'Robert',
	    'last': 'Smith',
	    'phone': 441415546654
	})

def phonebook_put_model(key_name='bob'):
	pb = phonebook();
	if pb is None: return False

	PhoneBookModel = pb.get_model()

	model = PhoneBookModel()
	model.key = key_name
	model.first = 'Edward'
	model.last = 'Holmes'
	model.phone = 234895779345

	saved = pb.put(model)
	print 'saved', model.key, saved

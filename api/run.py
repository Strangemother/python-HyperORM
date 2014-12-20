from service import Service
import service
import core
import spaces
from core import models

from examples.phonebook import phonebook_put_model
import tools

def boot():
    print 'Performing initial routines. Run the following DEV setup\n---'
    print 'hyperdex', tools.install_coordinator()
    print 'hyperdex', tools.install_daemon()

def install():
    s = Service()
    is_installed = s.installed()
    print 'installed', is_installed

    if is_installed is not True:
        print 'performing install'
        installed = s.install()
        print 'installed', installed

def model():
    print 'Model', models.Model().get_attrs()
    print 'Model', models.Model().get_def()
    print 'InstallModel', models.InstallModel().get_attrs()
    print 'InstallModel', models.InstallModel().get_def()
    print 'DocumentModel', models.DocumentModel().get_attrs()
    print 'DocumentModel', models.DocumentModel().get_def()
    print 'NamedInstallModel', models.NamedInstallModel().get_def()
    print 'NamedInstallModel', models.NamedInstallModel().get_attrs()
    print 'AllTypesModel', models.AllTypesModel().get_def()
    print 'AllTypesModel', models.AllTypesModel().get_attrs()

def space():
    a = spaces.AllTypes()
    d = spaces.Phonebook()
    e = spaces.FriendList()
    f = spaces.UserLock()
    print '\n--- space ---\n'
    print a.hyper_def()
    print '\n--- space ---\n'
    print d.hyper_def()
    print '\n--- space ---\n'
    print e.hyper_def()
    print '\n--- space ---\n'
    print f.hyper_def()

def process():
    p =  spaces.Process()
    print 'Current:', p.list_spaces()


if __name__ == '__main__':
    boot()
    process()
    phonebook_put_model()

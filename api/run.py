from service import Service
import service
import core
import spaces
from core import models

import tools

def boot():
    print tools.install_coordinator()
    print tools.install_daemon()

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
    print 'Process', p.list_spaces()

def phonebook():
    sv = Service()
    pb = spaces.Phonebook(sv)
    installed = pb.installed()

    if installed is False:
        print 'Install phonebook'
        installed = pb.install()

    if installed is False:
        print 'Could not install phonebook'

    return pb

if __name__ == '__main__':
    boot()
    process()
    pb = phonebook()

    import pdb; pdb.set_trace()
    removed = pb.remove()
    print 'removed phonebook space:', removed

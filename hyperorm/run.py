from api import service, core, spaces
from api.service import Service
from api.core import models

from examples.phonebook import phonebook_put_model
from api import tools


def boot():
    print 'Initial console routines:\n'
    co = tools.install_coordinator()
    da = tools.install_daemon()
    print 'hyperdex', co
    print 'hyperdex', da
    return [co, da]


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
    p = spaces.Process()
    print 'Current:', p.list_spaces()


if __name__ == '__main__':
    boot()
    process()
    phonebook_put_model()

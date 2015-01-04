from ..api import tools
from .. import settings
import os
from blessings import Terminal

t = Terminal()

def main():

    for i, daem in enumerate(settings.DAEMONS):

        print "{t.green}Starting Daemon: {t.bold}{i}{t.normal}".format(t=t, i=i)
        print "{t.green}LISTEN_IP: {t.bold}{d}{t.normal}".format(t=t, d=daem['LISTEN_IP'])
        print "{t.green}LISTEN_PORT: {t.bold}{d}{t.normal}".format(t=t, d=daem['LISTEN_PORT'])
        print "{t.green}COORDINATOR PORT: {t.bold}{d}{t.normal}".format(t=t, d=daem['COORDINATOR_PORT'])
        print "{t.green}COORDINATOR: {t.bold}{d}{t.normal}".format(t=t, d=daem['COORDINATOR_IP'])

        co = tools.install_daemon(
            listen_ip= daem['LISTEN_IP'],
            listen_port= daem['LISTEN_PORT'],
            coord_port= daem['COORDINATOR_PORT'],
            coord_ip= daem['COORDINATOR_IP'],
            )
        s = 'hyperdex %s' % co
        break
    os.system(s)

if __name__ == '__main__':
    main()

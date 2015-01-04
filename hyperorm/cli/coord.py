from ..api import tools
from .. import settings
import os
from blessings import Terminal

t = Terminal()

def main():

    for i, coord in enumerate(settings.COORDINATORS):
        print "{t.green}Starting coordinator: {t.bold}{i}{t.normal}".format(t=t, i=i)
        print "{t.green}IP: {t.bold}{d}{t.normal}".format(t=t, d=coord['IP'])
        print "{t.green}PORT: {t.bold}{d}{t.normal}".format(t=t, d=coord['PORT'])
        print "{t.green}CLUSTER PORT: {t.bold}{d}{t.normal}".format(t=t, d=coord['CLUSTER_PORT'])
        print "{t.green}CLUSTER: {t.bold}{d}{t.normal}".format(t=t, d=coord['CLUSTER_IP'])

        co = tools.install_coordinator(
            ip= coord['IP'],
            port= coord['PORT'],
            cluster_port= coord['CLUSTER_PORT'],
            cluster= coord['CLUSTER_IP'],
            )
        s = 'hyperdex %s' % co
        break
    os.system(s)

if __name__ == '__main__':
	main()

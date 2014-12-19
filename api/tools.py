from settings import *
from core.interactions import ProcessMixin

import os
import errno

def makedirs_exist(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def install_coordinator(ip='127.0.0.1', port=1982, cluster=None, cluster_port=None):
	# hyperdex coordinator -f -l 127.0.0.1 -p 1982 --daemon

	# daemon
	# -d, --daemon                run in the background
	# -f, --foreground            run in the foreground
	# -D, --data=dir              store persistent state in this directory (default: .)
	# -L, --log=dir               store logs in this directory (default: --data)
	# -l, --listen=IP             listen on a specific IP address (default: auto)
	# -p, --listen-port=port      listen on an alternative port (default: 1982)
	# -c, --connect=addr          join an existing cluster through IP address or hostname
	# -P, --connect-port=port     connect to an alternative port (default: 1982)
	#     --pidfile=file          write the PID to a file (default: don't)
	print 'install coordinator'

	pid_path = os.path.join(PID_DIR, 'cood_pid')
	makedirs_exist(LOG_DIR)
	makedirs_exist(COORD_DATA_DIR)
	# make path
	cmds = ['coordinator',
		'--data', COORD_DATA_DIR,
		'--log', LOG_DIR,
		'--daemon'
	]

	if ip is not None: cmds = cmds + ['--listen', ip]
	if port is not None: cmds = cmds + ['--listen-port', str(port)]
	if cluster is not None: cmds = cmds + ['--connect', cluster]
	if cluster_port is not None: cmds = cmds + ['--connect-port', str(cluster_port)]

	cmds = cmds + ['--pidfile', pid_path]
	print ' '.join(cmds)


def install_daemon(listen_ip='127.0.0.1', listen_port=2012, \
	coord_ip=None, coord_port=1982):
    # The HyperDex daemons are the workhorse processes
    # that actually house the data in the data store and
    # respond to client requests.
    # start a daemon on
    # the the same machine as the coordinator
    #
    # The last argument is a pointer to a directory where
    # the daemon will store all data. Each HyperDex daemon must
    # have its own data directory.

	# It doesn
	# w4t hurt to start a few more daemon instances at this point

	#   -d, --daemon                    run in the background
	#   -f, --foreground                run in the foreground
	#   -D, --data=dir                  store persistent state in this directory (default: .)
	#   -L, --log=dir                   store logs in this directory (default: --data)
	#       --pidfile=file              write the PID to a file (default: don't)
	#   -l, --listen=IP                 listen on a specific IP address (default: auto)
	#   -p, --listen-port=port          listen on an alternative port (default: 1982)
	#   -c, --coordinator=addr          join an existing HyperDex cluster through IP address or hostname
	#   -P, --coordinator-port=port     connect to an alternative port on the coordinator (default: 1982)
	#   -t, --threads=N                 the number of threads which will handle network traffic
	#
	# Help options:
	#   -?, --help                      Show this help message
	#       --usage                     Display brief usage message
	print 'install daemon'

	pid_path = os.path.join(PID_DIR, 'daemon_pid')
	makedirs_exist(LOG_DIR)
	makedirs_exist(DAEMON_DATA_DIR)
	makedirs_exist(PID_DIR)
	# make path
	cmds = ['daemon',
		'--data', DAEMON_DATA_DIR,
		'--log', LOG_DIR,
		'--daemon'
	]

	if listen_ip is not None:
		cmds = cmds + ['--listen', listen_ip]

	if listen_port is not None:
		cmds = cmds + ['--listen-port', str(listen_port)]

	if coord_ip is not None:
		cmds = cmds + ['--coordinator', coord_ip]

	if coord_port is not None:
		cmds = cmds + ['--coordinator-port', str(coord_port)]

	cmds = cmds + ['--pidfile', pid_path]
	# run command LOG_DIR
	print ' '.join(cmds)

import os

# The name of the API app created. Changing this will also change the
# default DATA, PIDS, and LOGS path
APP_NAME = 'hyperdex-api-core'

# Base root
API_DIR = os.path.dirname(__file__)

# hpme user local
USER_DIR = os.path.expanduser('~')

# The ip address to listen to. this is not defined as the default is 'auto'
# 127.0.0.1

# LISTEN_IP = 'auto'
APP_DIR = os.path.join(USER_DIR, APP_NAME)

# Location to store the data
DATA_DIR = os.path.join(APP_DIR, 'DATA', )

# Location to store the pids
PID_DIR = os.path.join(DATA_DIR, 'pids')


# Coor data store (relative to DATA)
COORD_DATA_DIR = os.path.join(DATA_DIR, 'coord')

DAEMON_DATA_DIR = os.path.join(DATA_DIR, 'daemon')
# Log data store
LOG_DIR = os.path.join(DATA_DIR, 'logs')

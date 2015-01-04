from api.settings import *

COORDINATORS = (
	{
		'IP': '127.0.0.1',  # Listen to port
		'PORT': 1982,
		'CLUSTER_IP': None, # Existing cluster IP
		'CLUSTER_PORT': None
	},
)

DAEMONS = (
	{
		'COORDINATOR_IP': '127.0.0.1',  # Listen to port
		'COORDINATOR_PORT': 1982,
		'LISTEN_IP': None, # Existing cluster IP
		'LISTEN_PORT': None
		# 'THREADS': 4
	},
)

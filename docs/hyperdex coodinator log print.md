# hyperdex coodinator log print:


Log file created at: 2014/12/09 17:36:07
Running on machine: three.strangemother.com
Log line format: [IWEF]mmdd hh:mm:ss.uuuuuu threadid file:line] msg
I1209 17:36:07.866830 23255 daemon.cc:351] started new cluster from command-line arguments: configuration(cluster=5453945523694809888, prev_token=0, this_token=5686642700536017622, version=1, command=[12416784560885354555], config=[12416784560885354555], members=[chain_node(bind_to=127.0.0.1:1982, token=12416784560885354555)])
I1209 17:36:07.870136 23259 object_manager.cc:1032] spawning worker thread for object 7528171833139684728
I1209 17:36:07.871482 23255 daemon.cc:611] initializing hyperdex with "/usr/lib/hyperdex/hyperdex-1.3.0/libhyperdex-coordinator.so.0.0.0"
I1209 17:36:07.871547 23255 daemon.cc:625] resuming normal operation
I1209 17:36:07.871567 23255 daemon.cc:1284] deploying configuration configuration(cluster=5453945523694809888, prev_token=0, this_token=5686642700536017622, version=1, command=[12416784560885354555], config=[12416784560885354555], members=[chain_node(bind_to=127.0.0.1:1982, token=12416784560885354555)])
I1209 17:36:07.871738 23255 daemon.cc:1341] the latest stable configuration is configuration(cluster=5453945523694809888, prev_token=0, this_token=5686642700536017622, version=1, command=[12416784560885354555], config=[12416784560885354555], members=[chain_node(bind_to=127.0.0.1:1982, token=12416784560885354555)])
I1209 17:36:07.871752 23255 daemon.cc:1342] the latest proposed configuration is configuration(cluster=5453945523694809888, prev_token=0, this_token=5686642700536017622, version=1, command=[12416784560885354555], config=[12416784560885354555], members=[chain_node(bind_to=127.0.0.1:1982, token=12416784560885354555)])
W1209 17:36:07.871760 23255 daemon.cc:1348] the most recently deployed configuration can tolerate at most 0 failures which is less than the 2 failures the cluster is expected to tolerate; bring 4 more servers online to restore 2-fault tolerance
I1209 17:36:07.871767 23255 daemon.cc:2078] we are chain_node(bind_to=127.0.0.1:1982, token=12416784560885354555) and here's some info: issued <=3 | acked <=3
I1209 17:36:07.871773 23255 daemon.cc:2081] our stable configuration is configuration(cluster=5453945523694809888, prev_token=0, this_token=5686642700536017622, version=1, command=[12416784560885354555], config=[12416784560885354555], members=[chain_node(bind_to=127.0.0.1:1982, token=12416784560885354555)])
I1209 17:36:07.871779 23255 daemon.cc:2082] the suffix of the chain stabilized through 0
I1209 17:36:07.871790 23255 daemon.cc:2346] command tail stabilizes at configuration 1
I1209 17:36:07.871930 23259 object_manager.cc:1104] hyperdex:init @ 2: initializing HyperDex cluster with id 6967713747038391075
I1209 17:36:07.871940 23259 object_manager.cc:1104] hyperdex:init @ 2: issuing new configuration version 1
I1209 17:36:07.871945 23259 object_manager.cc:1104] hyperdex:init @ 2: acked through version 1
I1209 17:36:07.871950 23259 object_manager.cc:1104] hyperdex:init @ 2: stable through version 1
I1209 17:36:38.001247 23259 object_manager.cc:1104] hyperdex:alarm @ 3: establishing checkpoint 1
I1209 17:36:38.001308 23259 object_manager.cc:1104] hyperdex:alarm @ 3: checkpoint 1 done
I1209 17:37:00.000349 23255 daemon.cc:2078] we are chain_node(bind_to=127.0.0.1:1982, token=12416784560885354555) and here's some info: issued <=4 | acked <=4
I1209 17:37:00.000427 23255 daemon.cc:2081] our stable configuration is configuration(cluster=5453945523694809888, prev_token=0, this_token=5686642700536017622, version=1, command=[12416784560885354555], config=[12416784560885354555], members=[chain_node(bind_to=127.0.0.1:1982, token=12416784560885354555)])
I1209 17:37:00.000442 23255 daemon.cc:2082] the suffix of the chain stabilized through 1
I1209 17:37:08.250612 23259 object_manager.cc:1104] hyperdex:alarm @ 4: establishing checkpoint 2

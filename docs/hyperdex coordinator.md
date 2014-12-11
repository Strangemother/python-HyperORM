hyperdex coordinator -f -l 127.0.0.1 -p 1982

I1209 17:32:52.043732 23222 daemon.cc:307] running in the foreground
I1209 17:32:52.043946 23222 daemon.cc:308] no log will be generated; instead, the log messages will print to the terminal
I1209 17:32:52.044036 23222 daemon.cc:309] provide "--daemon" on the command-line if you want to run in the background
I1209 17:32:52.048583 23222 daemon.cc:351] started new cluster from command-line arguments: configuration(cluster=17571032612712820954, prev_token=0                                                                            , this_token=11508132490459778633, version=1, command=[2603668735669183251], config=[2603668735669183251], members=[chain_node(bind_to=127.0.0.1:198                                                                            2, token=2603668735669183251)])
I1209 17:32:52.051586 23226 object_manager.cc:1032] spawning worker thread for object 7528171833139684728
I1209 17:32:52.053050 23222 daemon.cc:611] initializing hyperdex with "/usr/lib/hyperdex/hyperdex-1.3.0/libhyperdex-coordinator.so.0.0.0"
I1209 17:32:52.053127 23222 daemon.cc:625] resuming normal operation
I1209 17:32:52.053158 23222 daemon.cc:1284] deploying configuration configuration(cluster=17571032612712820954, prev_token=0, this_token=11508132490                                                                            459778633, version=1, command=[2603668735669183251], config=[2603668735669183251], members=[chain_node(bind_to=127.0.0.1:1982, token=260366873566918                                                                            3251)])
I1209 17:32:52.053349 23222 daemon.cc:1341] the latest stable configuration is configuration(cluster=17571032612712820954, prev_token=0, this_token=                                                                            11508132490459778633, version=1, command=[2603668735669183251], config=[2603668735669183251], members=[chain_node(bind_to=127.0.0.1:1982, token=2603                                                                            668735669183251)])
I1209 17:32:52.053367 23222 daemon.cc:1342] the latest proposed configuration is configuration(cluster=17571032612712820954, prev_token=0, this_toke                                                                            n=11508132490459778633, version=1, command=[2603668735669183251], config=[2603668735669183251], members=[chain_node(bind_to=127.0.0.1:1982, token=26                                                                            03668735669183251)])
W1209 17:32:52.053380 23222 daemon.cc:1348] the most recently deployed configuration can tolerate at most 0 failures which is less than the 2 failur                                                                            es the cluster is expected to tolerate; bring 4 more servers online to restore 2-fault tolerance
I1209 17:32:52.053391 23222 daemon.cc:2078] we are chain_node(bind_to=127.0.0.1:1982, token=2603668735669183251) and here's some info: issued <=3 |                                                                             acked <=3
I1209 17:32:52.053400 23222 daemon.cc:2081] our stable configuration is configuration(cluster=17571032612712820954, prev_token=0, this_token=1150813                                                                            2490459778633, version=1, command=[2603668735669183251], config=[2603668735669183251], members=[chain_node(bind_to=127.0.0.1:1982, token=26036687356                                                                            69183251)])
I1209 17:32:52.053410 23222 daemon.cc:2082] the suffix of the chain stabilized through 0
I1209 17:32:52.053421 23222 daemon.cc:2346] command tail stabilizes at configuration 1
I1209 17:32:52.053570 23226 object_manager.cc:1104] hyperdex:init @ 2: initializing HyperDex cluster with id 4471993731801203209
I1209 17:32:52.053585 23226 object_manager.cc:1104] hyperdex:init @ 2: issuing new configuration version 1
I1209 17:32:52.053591 23226 object_manager.cc:1104] hyperdex:init @ 2: acked through version 1
I1209 17:32:52.053598 23226 object_manager.cc:1104] hyperdex:init @ 2: stable through version 1
I1209 17:33:00.000849 23222 daemon.cc:2078] we are chain_node(bind_to=127.0.0.1:1982, token=2603668735669183251) and here's some info: issued <=3 | acked <=3
I1209 17:33:00.001086 23222 daemon.cc:2081] our stable configuration is configuration(cluster=17571032612712820954, prev_token=0, this_token=11508132490459778633, version=1, command=[2603668735669183251], config=[2603668735669183251], members=[chain_node(bind_to=127.0.0.1:1982, token=2603668735669183251)])
I1209 17:33:00.001183 23222 daemon.cc:2082] the suffix of the chain stabilized through 1

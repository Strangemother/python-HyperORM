http://symas.com/mdb/hyperdex2/

# Dev requirements:


## libsodium

For authorization, libmaracroons provides the object security based upon:

https://github.com/rescrv/libmacaroons

This should install fine, and may also be provided with the HyperDex installation. 

Performing manual installation may require additional apps not listed within the libmacaroons documentation.

You may need required tools:

    sudo apt-get install build-essential python-dev
    sudo apt-get install autoconf
    sudo apt-get install pkg-config 

You'll need a functioning GCC compiler *build essential* and a recent version of libSodium:

    wget https://download.libsodium.org/libsodium/releases/libsodium-1.0.1.tar.gz
    tar xzvf libsodium-1.0.1.tar.gz
    cd libsodium-1.0.1
    ./configure --enable-python-bindings && make && make check
    sudo make install 

If all dependencies are met, documentation implemented version of macaroons is easy:

    wget http://hyperdex.org/src/libmacaroons-0.2.0.tar.gz
    tar xzf libmacaroons-0.2.0.tar.gz
    cd libmacaroons-0.2.0
    ./configure
    make
    sudo make install


# Running hyperdex

run the coordinator in it's own folder (keep it clean)

preferably:

    /hyperdex-api-core/coord

    $ hyperdex coordinator -f -l 127.0.0.1 -p 1982 --daemon

    I1209 17:36:07.860146 23254 daemon.cc:273] forking off to the background
    I1209 17:36:07.860347 23254 daemon.cc:274] you can find the log at ./replicant-daemon-YYYYMMDD-HHMMSS.sssss
    I1209 17:36:07.860438 23254 daemon.cc:275] provide "--foreground" on the command-line if you want to run in the foreground

See the print in `hyperdex coodinator log print`

Next run a daemon preferably:

    /hyperdex-api-core/daem

    $ hyperdex daemon -f

read hyperdex_daemon.md for a nice output 

We're ready for python:

    from hyperdex import admin, client
    import hyperdex.admin
    
    a = admin.Admin('127.0.0.1', 1982)

    $ hyperdex coordinator -f -l 127.0.0.1 -p 1982 --daemon
    $ hyperdex daemon -f --listen=127.0.0.1 --listen-port=2012 \
    --coordinator=127.0.0.1 --coordinator-port=1982 --data=/hyperdex_data

    I1209 16:49:51.644667 22079 daemon.cc:298] running in the foreground
    I1209 16:49:51.644884 22079 daemon.cc:299] no log will be generated; instead, the log messages will print to the terminal
    I1209 16:49:51.644978 22079 daemon.cc:300] provide "--daemon" on the command-line if you want to run in the background
    I1209 16:49:51.645062 22079 daemon.cc:307] initializing local storage
    I1209 16:49:51.650259 22079 daemon.cc:362] generated new random token:  10426080285352428648
    I1209 16:49:51.650714 22085 background_thread.cc:154] wiping thread started
    I1209 16:49:51.650816 22084 background_thread.cc:154] indexing thread started
    I1209 16:49:51.650902 22083 background_thread.cc:154] checkpointer thread started

    from hyperdex import admin, client
    import hyperdex.admin
    
    a = admin.Admin('127.0.0.1', 1982)
    a.add_space('''
      space phonebook
      key username
      attributes first, last, int phone
      subspace first, last, phone
      create 8 partitions
      tolerate 2 failures
      ''')
      True

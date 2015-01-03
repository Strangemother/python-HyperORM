# Getting Started

Before the fun of reading and writing data, we need to ensure we're setup.
HyperDex needs a few things working before we can simply press run - Let's do the Basics.

> Granted this is not ideal - but HyperDex provides some great tools and we're focusing on the API to write data *Future builds can cater for simpler installs*

## First time run

Run the api method `run.boot()` to ensure your settings are prepared for the hyprdex to run manually.

A please print will prompt you to run the service in the right method.

If you've got settings (we'll cover this later) they'll be picked up for the formatted print out for you to copy paste.

````python
>>> import run
>>> run.boot()
Performing initial routines. Run the following DEV setup
---
hyperdex coordinator --data /foo/DATA/coord --log /foo/DATA/logs -f --listen 127.0.0.1 --listen-port 1982 --pidfile /foo/DATA/pids/cood_pid
hyperdex daemon --data /foo/DATA/daemon --log /foo/DATA/logs -f --listen 127.0.0.1 --listen-port 2012 --coordinator-port 1982 --pidfile /foo/DATA/pids/daemon_pid
>>>
```
Those strings are ready to paste into the console for the basic hyperdex.


## Example Space

Before we begin building our super cool super quick giant JSON cluster, lets follow some examples:

> The provided examples are designed to follow the HyperDex Docs with their provided examples, You're encoraged to read their documentation too.

Lets get the demo `phonebook` space. When you run this method the first time, it will install. **This only happens on provided demos*

```python
>>> from examples import phonebook
>>> phonebook()
Install phonebook
<spaces.Phonebook object at 0x7fd432244490>
>>>
```

The examples are designed to install when created. Their made for temporary use and should be deleted from any live server.

#### What just happened?

Okay, explicit is important - These demos are designed to be quick to use. If you're itching to see how it was installed - This is the code provided for you. Beware, It's chunky...

```python
from service import Service
from spaces import Phonebook

sv = Service()
pb = Phonebook(sv)
installed = pb.installed()

if installed is False:
    print 'Install phonebook'
    installed = pb.install()

if installed is False:
    print 'Could not install phonebook'
```
Okay, so this very simple. But what is this for? Surely HyperDex provides a simply install routine? Yes, but we've also covered some basics (we'll cover later):

1. Connect a client and (in this case) an admin client to the HypderDex coordinator (on port `1982`)
2. Write HyperDex required string definition for the space creation. Our model creates and installs this.
3. Space definition has been checked for a valid install and is ready to go.
4. A 'client' is provided for you to comminicate with your cluster and write data.

So much to do! But do consider the benifits of your very own hyper cluster. Better still - it's done for you!

### Cleanup

When finished with your hyper space **Clean it up**. There is nothin worse than a grubby developer. This is why we can't have nice things.

```python
# remove the phonebook from the hyper space
pb.remove() # True
```

## Getting a model

Okay great. We have a new model. If you were to import the example again, it will not install again. Let's recap (with our without the example):

With the example runner:

```python
from examples import phonebook
pb = phonebook()
```

In a more verbose setup - you can get any space. In this case, we'll still import a `Phonebook` space:

```python
from service import Service
from spaces import Phonebook

sv = Service(ip='127.0.0.1', port=1982)
pb = Phonebook(service=sv)
pb.installed() # True
```

Fundamentally you need a `Service` object to talk to the cluster. this is a tool wrapping the HyperDex `client` and `admin` objects. Providing a service to the space `Phonebook` allows read, write. With admin permissions, it can be installed.

You can change a `service`, pointing to another cluster very easily. The new `Service` object can refer to another `IP` and `port` for an alterative coordinator

---

We're now ready to talk to the cluster.


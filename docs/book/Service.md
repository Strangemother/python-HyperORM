# Service

A Service defines The Hyperdex connection. This lightly wraps the service admin and client. Using the service You can check for a service, and check for the auto space used for Space definition alteration monitoring.

An easy way to persist the API space is by performing an install script such as:

```python
def install():
    s = Service()
    is_installed = s.installed()
    print 'installed', is_installed

    if is_installed is not True:
        print 'performing install'
        installed = s.install()
        print 'installed', installed
```


## Usage

```python
s = Serivce(ip='127.0.0.1', port=1982)
s.install_space()
client = s.get_client()
```

# Making a Space

Your HyperDex cluster is built of Clusters and Spaces.

You need a Space and a Model and Service

The service allows a connection to a HyperDex cluster

```python
>>> from service import Service
>>> srv=Service()
```

Instansiate your model, passing it's service as the first argument.

```python
>>> from spaces import Phonebook
>>> pbs = Phonebook(srv)
```

We can check if space is installed

```python
>>> pbs.installed()
False
```

It isn't so we should install it.

```python
>>> pbs.install()
True
```

In the background - the API wrote the HyperDex string to the add_space core interface. You can read the definition for yourself:

```python
>>> pbs.hyper_def()
'space phonebook\nkey pk\nattributes\nint phone,\nstring last,\nstring first\ntolerate 2 failures\ncreate 8 partitions'
>>> pbs.installed()
True
```


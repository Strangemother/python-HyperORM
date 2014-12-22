# Hyperdex python API wrapper

Hyperdex is a clever fast key value storage system.
To make it easier to develop upon, the API provides a basic class structure for managing and maintaining the spaces and its data.

Much of the supplied hyperdex python API is lightly wrapped to provide:

+ Space definitions with install management
+ in out data routines
+ model structures with python exposure

The service allows a connection to a HyperDex cluster

```python
from service import Service
srv=Service()
```

Instansiate your model, passing it's service as the first argument.

```python
from spaces import Phonebook
space = Phonebook(srv)
```

The HyperDex string adds to the add_space core interface. You can read the definition for yourself:

```python
>>> space.hyper_def()
'space phonebook\nkey pk\nattributes\nint phone,\nstring last,\nstring first\ntolerate 2 failures\ncreate 8 partitions'
>>> space.install()
True
>>> space.installed()
True
```

Use can use the original client, provided the through the `Service` object we gave to the new `Phonebook`:

```python
>>> space.service.client.put('phonebook', 'bob', {
    'first': 'Robert',
    'last': 'Smith',
    'phone': 441415546654
})
```

---

The client is agnostic to service and API layer. Now lets use the API service:
```
>>> space.service.client.get('bob')
{'phone': 441415546654, 'last': 'Smith', 'first': 'Robert'}
```

We can get the required model from the space `Phonebook`. This ensures when we `save()` we have an attached Space for our model to save to.

```python
>>> M = space.get_model()
>>> bob = M('bob', first='David', last='Arnolf', phone=440743566523)
>>> bob.last = 'Arnold' # Seplling*
>>> bob.save()
True
```

Done! we got our model type `PhonebookModel` and saved the values. The model knows where to be saved as it has an associated space and service.


```python
>>>  bob = space.get('bob')
<models.PhoneBookModel object at 0x7f9235716dd0>
```

Great! it's as easy as the original client object. Plus we get a `Model` object we can implement through the API.
With a `Model` We can change and save the the data and use the Model builtin `save`. This performs a `put` to the service client alike the example above:

```python
>>> bob.first
'Robert'
>>> bob.phone
234895779345L
>>> bob.last = 'Ducker'
>>> bob.save()
True
```

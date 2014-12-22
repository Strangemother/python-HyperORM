# Get/Set to Space

We can get a space. First we need data in the cluster before we can read it.

```python
>>> from spaces import Phonebook
>>> from service import Service
>>> space=Phonebook(Service())
```

## Using the client

Let's have a go with the raw HyperDex connection. This allows us to write arbitrary JSON like objects to the service. The client (client and admin connections to the host HyperDex cluster) is provided by the HyperDex installed API.

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

Lets add another item; this time using model definitions.

## Using Models

We'll first cover how to save information to a cluser - it's exceptionally easy:

#### Save a new model

A model defines the fields of your data. We can create one without the need to define an object.
We'll create an entry called 'dave'.

We can get the required model from the space `Phonebook`. This ensures when we `save()` we have an attached Space for our model to save to.
```python
>>> M = space.get_model()
>>> m = M('dave', first='David', last='Arnolf', phone=440743566523)
>>> m.last = 'Arnold' # Seplling*
>>> m.save()
True
```

Done! we got our model type `PhonebookModel` and saved the values. The model knows where to be saved as it has an associated space and service

---

**Why do I need to define a space, surely thats automatic?**

A Space defines where to store your model. Although our model is specifically written for space, in the future you may wish to save a 'user' model to a 'business_users' and 'developer_users'. Additionally, a `Service` can be passed to the `save(service=None)` method. As you may wish to save this model though an Admin service or a client connected through a different IP.

---

```python
>>>  dave = space.get('dave')
<models.PhoneBookModel object at 0x7f9235716dd0>
>>>  bob = space.get('bob')
<models.PhoneBookModel object at 0x7f9235716de0>
```
Great! it's as easy as the original client object. Plus we get a `Model` object we can implement through the API.

```python
>>> bob.first
'Robert'
>>> bob.last
'Smith'
>>> bob.phone
234895779345L
```

With a `Model` We can change and save the the data and use the Model builtin `save`. This performs a `put` to the service client alike the example above:

```python
>>> bob.last = 'Ducker'
>>> bob.save()
True
```


We have a space - and we'll use the get method to return a model object.

```python
>>> from examples.phonebook import phonebook
>>> space = phonebook()
>>> m=space.get('bob')
>>> m.last
'Ducker'
>>> m.last = 'Ranger'
>>> m.save()
True
```

The **save()** method allows the changed model to be put back into the cluster.

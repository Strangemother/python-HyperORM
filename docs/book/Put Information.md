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

We'll first cover how to fetch information from a cluser - it's exceptionally easy:

```python
>>>  bob = space.get('bob')
<models.PhoneBookModel object at 0x7f9235716dd0>
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
'Smith'
>>> m.last = 'Ranger'
>>> m.save()
True
```

The **save()** method allows the changed model to be put back into the cluster.

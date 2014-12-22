# Models

A `Model` defines the fields used within a space.

A HyperDex Space requires a set of `attributes` the API maps to a `Model`. There are some basic types you can store to a Space.

We use a `Model` to set this up.

```python
class PhoneBookModel(Model):
    first = types.Str(index=True)
    last = types.Str(index=True)
    phone = types.Int(index=True)
```

This is a standard Model defining 3 fields.

You can simply work with a space on the command line:

```python
 >>> from models import *
 >>> pm = models.PhoneBookModel()
```

Each attribute to be installed into hyperdex is `types.*`. Our example installs two string fields `first, last` and an integer field `phone`

When this is provided to a Space`Space` It is converted to a HyperDex attributes string for the space definition.

### Index

On a field you define `index=true` applying another HyperDex index dimension to your Space. This is not trivial - but it allows for searching. In the example case we've create a *3 dimentional subspace*

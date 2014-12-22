# Spaces

The definition of a Hyperdex space implements as a model`Model` with associated values assigned to a space `Space`. A space is written to the hyperdex cloud as a place to store your key:values.

The Space is where you store your key values in a json like format. The wrapper provided simply helps write the stringly space definition as a class.


You're space defines a setup to create within Hyperdex. This is an example plucked from the Hyperdex documentation:

[HyperDex Quick Start](http://hyperdex.org/doc/latest/QuickStart/#sec:quick-start:space)

```python
class Phonebook(Space):
    name = 'phonebook'
    model = PhoneBookModel
    partitions = 8
    tolerate = 2
```

And it's assigned model of which we'll cover in another chapter.

```python
class PhoneBookModel(Model):
    first = types.Str(index=True)
    last = types.Str(index=True)
    phone = types.Int(index=True)
```

---

To simplify the understanding, consider a `Space` Like a normal SQL table. A `Model` is like a table row, full of data to be saved to the `Space`.

An example Space called `Phonebook` has attributes like `name` and `tolerate`. It's `Model` has fields like `phone`, `first` and `last` name.

In a usual Table structure the "fields" would be associated with the table. In our `Space`, our datas "fields" Are stored within the `Model`.

---

Not so hard. Next, lets expand our `Space` structure.

Inkeeping with our concept - the `Phonebook` has some fields associated with the data to be stored, and fields about how the Space works.

---

`Space.partitions` helps HyperDex setup the Space. Imagine your Table (Our 'Phonebook'), needs to be spread over many servers - to ensure your big list is quick to respond. the `partitions` value spreads the index across `x` many servers.

In this example, we would consider the `Phonebook` index `a-f` is on server 1, `g-p` is on server 2 and so on. We spread our data across many servers.


## Fields

A space applies a interactive HyperDex Space to install to the cluster. We provide it with basic properties and the API will handle the conversion needed to work with the HyperDex cluster.


### name

The name field provides a name for your to target when interacting with the space. The example Space `Phonebook` will allow `get('phonebook')`


### model

the HyperDex Space requires `attributes` to you'll need from your Space. We simply define a `Model` of which maps to `types` needed for HyperDex.

The `Model` types are easy and map to standard python primitives such as `Str, Int, Float` of which are python `str, int, float` respectively.


### paritions

Paritions specify how many slices of the data HyperDex will create. Spreading the data over many regions.

As a general rule, the number of partitions should be greater than the number of daemons that will ever join the cluster.

If partitions is not defined, HyperDex will partition the cluster into 256 regions.


### tolerate

HyperDex is designed to ensure fault tolerance. By defining a `tolerate` failure count, HyperDex will protect against loss of the data by replicating `x` times.

If you've set the `tolerate = 2`, Hyperdex will replicate the data *3x* because 2 failures can occur.

|HyperDex automatically repairs from this one remaining copy.

---

That's as difficult as it gets for large-scale-key-value-fault-tolerant-crazy-fast-cluster!

Next let's look at the `Models` to understand how to put together the format for your fields.

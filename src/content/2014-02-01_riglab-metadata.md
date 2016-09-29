Title: RigLab: Metadata
Description: Article on metadata and python magic methods.
Author: Cesar Saez
Tags: riglab, rnd, code

Hi folks,

This entry will be a bit techy, but not too much... stay with me! :)

## First, what is metadata?

Metadata is "data about data", it describes information about the contents of the
item itself or its components... it's a note for our selves, so we don't
have to figure out that information from scratch the next time.

_Metadata by example:_
Let's say we have an asset composed by several meshes and
we need to collect all of them by scripting on export.

* We can ask the user for the meshes (via selection or something) and that's it,
but that means we will need an user input on EVERY export... no batch processing,
bummer!

* We can try to filter the meshes looping through the hierarchy + some logic
(conditionals + naming convention stuff) until collect all of them, it might work,
but there is a risk of the validation logic not always being true.

Or...

* **We can use metadata!** saving a 'note' with the meshes' name each time the
user export them, so we have an user defined fallback for batch processing!

## Cool, but how?

Metadata can be stored anywhere, it could be embeded on an attribute/custom-parameter,
written on an external file (so we can read it outside the DCC), stored
in a database and so on...

Whatever you choose, it is important to define an unified system to do it
because your code will become quite messy with all those extra metadata calls.

## Here comes the magic!

Are you familiar with [python's magic methods](http://www.rafekettler.com/magicmethods.html)?
Did you know they can be extended?

I did just that and it works great!

I created a base class for containers (I mean, things that group things together),
its instances serialize whatever you pass as an attribute thanks to python's magic
methods.

So each time I write something like this:

```python
from wishlib.si import SIWrapper  # the base class I was talking about

selected_obj = Application.Selection(0)
foo = SIWrapper(selected_obj)
foo.bar = 'baz'
```

On `foo.bar = 'baz'`, `__setattr__` is called, `baz` is serialized
and stored as string in a custom parameter (Softimage's version of maya attributes).

Let's say I restart Softimage (fresh session) and type something like this:

```python
from wishlib.si import SIWrapper

selected_obj = Application.Selection(0)  # same selection
foo = SIWrapper(selected_obj)
print foo.bar  # 'baz'
```

When `foo` is instanciated its `__init__` method is called, reading the metadata
from the custom parameters and initializing its members, so when we call `foo.bar`
it's a valid member and returns the expected data.

I don't want to bother you with the [implementation details](https://github.com/csaez/wishlib/blob/master/wishlib/si/siwrapper.py) (take it with a grain of salt),
but I think it is a really cool way to serialize stuff without add too much overhead
to existing code.

There's a catch though, mutable data types mutates itself changing its own data, so
your extended `__setattr__` method will never be called unless you explicitly
update the entire thing.

I would love to know how you guys solve this kind of stuff :)

Cheers!

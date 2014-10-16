Title: Hard Reload
Author: Cesar Saez
Tags: code

Hi folks,

If you're a python developer this shouldn't be new for you, but I struggled
a lot with this back in the day and thought it might be helpful share
some of the lessons learned.

Each time you import a python module in a session it get cached in a global
dictionary called `sys.modules`, this helps to speedup things and allow a better
memory management. If you really need to refresh that cache for a specific module
(because of a code change or whatever) python provides a nice function
called `reload()`.

So far so good, it works great! The only 'problem' is that you must
explicitly call it, I mean, you must call it after each import.

### What about packages?

I often write my stuff as a package, and having to explicitly reload each
module could be cumbersome, not to mention having to remove those calls in
production code... I'm too lazy for that.

Fortunatelly there is a workaround!

As sys.modules is just a standard dictionary it's possible manipulate the
raw data by yourself. This can cause some side effects because you would
be messing with python's global state, but to be honest it has saved my
ass a couple of times.

USE AT YOUR OWN RISK.

    :::python
    import sys


    def hard_reload(package_name):
        for k in sys.modules.keys():
            if k.startswith(package_name):
                del sys.modules[k]

    hard_reload("my_super_package")

By the way, kudos to [Ángel Pavón](http://agedito.com) for the tip!

Cheers
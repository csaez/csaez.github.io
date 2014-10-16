Title: Notes on python testing
Author: Cesar Saez
Tags: code, thoughts, maya

Hi guys,

I've been rediscovering unit testing in python lately and wanted to share some notes about this, I hope you find them useful.

There we go!

## Why use an unit testing framework?

One word: Convenience

You can always run your tests manually, but the harder to run tests, the less
likely you run them.

A piece of advice: be lazy, automate all the things! or even better: pick an
existing framework and stick with it.

## Nose

[Nose](http://nose.readthedocs.org/en/latest/) is a testing framework for python, it's not included in the standard library but that's ok for me (otherwise look for `unittest`).

## Why `nose` over `unittest`?

* Autodiscovering: put test functions in a module called `something_tests.py` and nose will find and run them for you.
* No boiler plate: write your test as a simple function and call it
`test_ something`, there's no need of inheritance from base classes or
decoration of your functions.
* Coverage: testing without coverage == no fun, more on this later.
* Plugins: nose provides a nice plugin architecture, as a consecuence there
are many useful extensions out there (`nose-watch` seems specially handy, check
out the project [here](https://github.com/lukaszb/nose-watch))... and of
course you might be able to extend it creating your own plugins.
* Things to come...

### Cool, how do I install `nose`?

    pip install nose

Once installed run `nosetests` in a terminal (from the root of your project) to run the tests.

> Do yourself a favor and install your dependencies in a `virtualenv`.

### Wait... virtual-what?

Ok, `virtualenv` creates an isolated python environment for your project... think of it as a custom `site-packages` per project.

You should check out the [documentation](https://virtualenv.pypa.io/en/latest/index.html), but in a nutshell:


    ::bash
    # Install virtualenv
    pip install virtualenv

    # Create a clean virtual environment at my_env/
    # there's no need of --no-site-packages as it's deprecated.
    virtualenv my_env/

    # Activate my_env
    source my_env/bin/activate

    # Deactivate current environment
    deactivate


#### Too much typing?

There's `virtualenvwrapper` to make things easier, or you can create a bunch
of aliases and go with that... Just keep it simple and don't waste too much
time on this.

Here's what I'm using to activate an existing environment in my system (put
this in your `~/.bashrc`):

    ::bash
    # activate a virtualenv
    # usage: activate my_env/
    function activate() { source "$1"bin/activate ;}

## Back to testing: What testing looks like?

Assuming a project structure like this:

    * my_proj
        * tests
            * __init__.py
            * rocket_science_tests.py
        * __init__.py
        * rocket_science.py

... where `rocket_science.py`:

    ::python
    def add_integers(*arg):
        if all([isinstance(i, int) for i in arg]):
            return sum(arg)
        raise TypeError("(%s) not an integer." % ",".join(arg))

then `rocket_science_tests.py` should look something like this:

    ::python
    import my_proj.rocket_science as rs


    def test_add_integers():
        assert rs.add_integers() == 0
        assert rs.add_integers(1) == 1
        assert rs.add_integers(3, 2) == 5
        assert rs.add_integers(5, -2) == 3
        assert rs.add_integers(0, -3) == -3

        try:
            rs.add_integers(3.14159, 1.61803)
        except Exception as err:
            assert type(err) == TypeError  # too much awesomeness?!

## What about coverage?

Coverage basically tells you how much of your code is covered by your tests, so 100% coverage means every line of code is tested at least once.

But there's more, it not only tells you the percentage but also the lines of code not covered (per module), so you can check this information and write more tests until reach the 100%.

## How can I check my coverage?

First...

    ::bash
    pip install coverage

and then add a couple of flags to `nosetests`:

    ::bash
    nosetests --with-coverage

... but it's taking into acount external modules! How to fix it?

    ::bash
    nosetests --with-coverage --cover-package=my_proj

#### Too much typing?

Again, here's what I'm using at the moment (put this in your `~/.bashrc`):

    ::bash
    # run nosetest with coverage
    # usage: testme (from the root of your project)
    function testme() { nosetests --with-coverage --cover-package="${PWD##*/}" ;}

## That's nice, but what about DCC code?

DCC code usually have strong dependencies on dynamic libraries initialized by
the DCC at runtime, this means we can only run our code within the DCC.

> Autodesk Maya has the ability to run in standalone mode, allowing us to
> execute our code without the overhead of a fully fledged app, but this is a
> quite unique feature compared to other DCCs.
> 
> There are interesting projects to automate testing for Maya-like apps
> ([dccautomation](https://github.com/rgalanakis/dccautomation) by Rob
> Galanakis looks promising).

### `mock` to the rescue!

`mock` is a library for testing in Python. It allows you to replace parts of
your system under test with mock objects and make assertions about how they
have been used.
Check out the docs [here](http://www.voidspace.org.uk/python/mock/index.html).

### How to intall mock?

    pip install mock

> `mock` is part of the standard library from python 3.3 onwards.

### ... and now what?

Let's say you want to test a snippet like this (standard Maya code):

    ::python
    from maya import cmds


    def get_bbox(obj_list):
        """
        Returns the bounding box of a list of objects. The values returned
        are in the following order: xmin ymin zmin xmax ymax zmax.
        """
        bbs = [cmds.xform(o, q=True, bb=True) for o in obj_list]
        return tuple([(min, max)[int(i >= 3)](x) for i, x in enumerate(zip(*bbs))])


    # test function intended to be executed within Maya
    def test_get_bbox():
        locs = cmds.spaceLocator(p=(0.5, 0.5, 0.5))
        locs.extend(cmds.spaceLocator(p=(-0.5, -0.5, -0.5)))
        assert get_bbox(locs) == (-1.5, -1.5, -1.5, 1.5, 1.5, 1.5)
        cmds.delete(locs)

    test_get_bbox()


Ok, what do we really need to test here?

In my opinion we must test the algorithm, make sure that we are considering all objects in the `obj_list` and making the right choices between bounding boxes... we can assume `cmds.xform` is working fine, there's no need to test Maya commands (they have their own testsuite, I guess).

So, in order to run this test on system python the first thing to do is skip
the `ImportError` and then refactor the test function patching `cmds.xform`
through the `mock` library.

The following code runs perfectly in system python. Note that, except for the
test function, everything else is the same as before:

    ::python
    try: from maya import cmds
    except ImportError: pass
    import mock


    def get_bbox(obj_list):
        """
        Returns the bounding box of a list of objects. The values returned
        are in the following order: xmin ymin zmin xmax ymax zmax.
        """
        bbs = [cmds.xform(o, q=True, bb=True) for o in obj_list]
        return tuple([(min, max)[int(i >= 3)](x) for i, x in enumerate(zip(*bbs))])


    @mock.patch("__main__.cmds", create=True)
    def test_get_bbox(cmds):
        return_values = {"loc1": (-0.5, -0.5, -0.5, 1.5, 1.5, 1.5),
                         "loc2": (-1.5, -1.5, -1.5, 0.5, 0.5, 0.5)}
        cmds.xform.side_effect = lambda *a, **k: return_values.get(a[0])
        assert get_bbox(["loc1", "loc2"]) == (-1.5, -1.5, -1.5, 1.5, 1.5, 1.5)

    test_get_bbox()

## Cool! but what's the point?

Being able to test our code from system python instead of the DCC makes a
__HUGE__ difference during testing! Run a test like this takes milliseconds
and we can automate the process through a testing framework like `nose`, so in
practical terms we can run tests everytime a file is saved without thinking too
much about it (take a look at `nose-watch`).

In contrast, be forced to open the DCC to run the testsuite, restart the
application to cleanup its global state and then repeat takes forever, making
the process a much less enjoyable experience.

At the end, testing is a powerful development tool, let's take advantage of it
to develop amazing tools!

Regards,
Cesar.
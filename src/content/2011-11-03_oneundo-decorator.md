Title: OneUndo decorator
Author: Cesar Saez
Tags: code, softimage

Hi folks,

I'm posting another entry from my old blog, this time it's a decorator
for Softimage that help us to wrap all the calls inside a function in an
unique undo.

The decorator itself should look something like this...

    from functools import wraps

    def OneUndo(function):
        @wraps(function)
        def _decorated(*args, **kwargs):
            try:
                Application.BeginUndo()
                f = function(*args, **kwargs)
            finally:
                Application.EndUndo()
                return f
        return _decorated

And a basic example...

    @OneUndo
    def CreateNulls(size=100):
        return [Application.ActiveSceneRoot.AddNull()
                for i in range(size)]

    CreateNulls()


Have Fun!

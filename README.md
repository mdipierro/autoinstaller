# autoinstaller

A package that automagically installs from PyPi everything you need as soon as you try import it.
For example, let's assume that you do not have the tornado web server.

    >>> import tornado
    Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
    ImportError: No module named tornado

But if you have autoinstaller

    >>> import autoinstaller
    >>> import tornado
    ...
    Processing dependencies for tornado
    ...
    Installed ...
    Finished processing dependencies for tornado
    >>>

And from now on the package can be used without existing or restarting the process.

Of course you must install autoinstaller first the old fashion way:

    >>> import autoinstaller

## License

BSD version 3
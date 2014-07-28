Title: QuickLauncher
Author: Cesar Saez
Tags: Tools, Softimage, code

{% img img-right {filename}images/quicklauncher.gif 250 %}
Hey folks,

Today I want to share a tool I've been using for a while, it's a simple
menu to search and launch softimage commnads and scripts (you can set
the script directory on the preferences).

In order to make it fast I'm caching the commands and script paths (just
the paths, the script itself is loaded on runtime), so if you add a new
script file or connect/disconnect workgroups please make sure that the
cache is reloaded (there's a command just for that) and everything
should be fine.

The menu requires [PyQtForSoftimage][1] and it's available [here][2].

Give it a try and let me know what you think :-)

Cheers!

[1]: http://github.com/caron/PyQtForSoftimage
[2]: http://github.com/csaez/quicklauncher
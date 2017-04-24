Title: DevManager: yet another plugin manager
Author: Cesar Saez
Tags: rnd, code

Hi folks,

I've been working on a manager for my developments, something like
softimage's plugin manager but better suited for my workflow (python
modules for the logic and pyQT for GUIs).

When I was working at [Kandor Graphics][1] we had some similar tools
(much more robust and sophisticated, of course), was one of the firsst
things they tackled and turned out to be an excellent decision on the
long run.

### Let's see some features...

`csDevManager` has 2 modes, the basic one works like a launcher for all my
custom commands, nothing too exciting here.

![csDevManager]({filename}images/csDevManager.jpg "csDevManager")

The developer mode is where it gets interesting, in this mode you can
see all the Addons/Developments and their plugins (including properties,
events and almost everything you can register on softimage).

Through the context menu you can access the reload function, this allow
you reload all python modules used in the addon, recompile the QT stuff
and reload the softimage's plugin in one click (big time saver).

You can also edit UI files (using QT Designer), explore directories,
create new addons, plugins and remove existing ones.

Another nice addition is a new sdk wizard with updated templates, this
makes really easy create new plugins.

And at last but not less, you have access to an API that allows you do
"everything" related to your addons, every you see in the GUI is doable
via API in a OOP way.

I've to do some clean up in order to make it completely generic, I'll
make a github repository with all my tools and share them as open source
ASAP.

Next step: work on my rigging framework using all I've learned in the
past years :)

Cheers!

[1]: http://www.kandorgraphics.com/en

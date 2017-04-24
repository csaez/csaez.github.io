Title: QuickLauncher v2.0
Author: Cesar Saez
Tags: code, tools

Hi folks,

I just wanted to let you know that I've updated [quicklauncher to v2.0](https://github.com/csaez/quicklauncher/releases/tag/v2.0).

A brief summary of the changes:

* This version is maya-only, you can still download the previous version from [here](https://github.com/csaez/quicklauncher/releases/tag/v1.0) though.
* There are no dependencies for general use (requires PySide but it's included with Maya >= 2014).
* The menu behaves like maya tab menu (node editor) but lists commands and user scripts instead of nodes.
* The auto-complete is based on QCompleter instead of me filtering QAction as in previous versions (cleaner, more stable, better).
* Settings are managed through QSettings instead of custom json files.
* There's a testsuite (92% coverage at the moment), so I will not break everything in each update.
* MIT license.

You can get `quicklauncher` from the [github repo](https://github.com/csaez/quicklauncher) as usual. Please be sure to read the readme, I did my best to explain everything you need to know before use it or contribute to the project.

Hope you like it,

Enjoy!

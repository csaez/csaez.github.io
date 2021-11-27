---

title: Amaranth v1.0
description: My first contribuition to a Blender plugin is out in the wild!
date: 2015-01-30
categories: [Projects]
tags: [blender]
toc: false

---
<!--more-->
Hi folks!

Last year was all about open source for me, I finally removed my Windows
partition and went full Linux (btw, gotta love [arch linux][arch]), also
decided to develop and share my projects under open source licenses (check out
my [github profile][gh]) and have been contributing to open source projects in
hopes of giving back to the community. This post is about the latter.

I just wanted to share that there's a new release of [Amaranth][a]: a
productivity addon for [Blender][bl] by [Pablo Vazquez][pb] (a.k.a. venomgfx).

I had always wanted to dive a bit deeper into [Blender][bl] and this project
seemed to be the perfect excuse to do it, so I gave it a try and decided to
[contribute][pr] by doing a much needed refactoring of the code base.

The project is now completely modular, so it is much easier to maintain and add
new features, each module registers/unregisters itself as long as it's imported
into the main file and everything just works.

So, that's it... if you're interested in [Blender][bl] please visit
[Amaranth][a]'s website and give it a try. I honestly think it's worth it :)

Cheers!

[arch]: https://www.archlinux.org/
[gh]: https://github.com/csaez
[bl]: http://www.blender.org
[a]: http://pablovazquez.org/amaranth/
[pb]: http://pablovazquez.org
[pr]: https://github.com/venomgfx/amaranth/pull/5

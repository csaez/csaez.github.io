Title: Working with pointcloud datasets
Author: Cesar Saez
Tags: softimage, code

Nowadays it's not that unusual having to work with scanned files (point
clouds), but most DCCs don't provide native support for those file formats
and we ended up whether using external converters or parsing ASCII files.

This entry is about the latter.

There's the quick and dirty approach, where we simply read the file and
create points (nulls, spheres, cubes, whatever) using those coordinates
via scripting, it works (sort of) in very simple scenarios, but it's not
reliable when dealing with large point clouds (and that's usually the case).

### Plan B: recreating a native icecache file!

Cache files [can be created using python][example]... but it's a bit
low-level and write such code kinda sucks!

Fortunatelly there's a not-so-known [python module][api] by Bradley Gabe
that provides a higher level API and free us from dealing with bytes,
data blocks, gzip and other boring stuff.

![Standford Bunny]({filename}images/stanford_bunny.jpg "Standford Bunny")

So, parsing a xyz file (like [this][bunny] stanford bunny) and write an
icecache file to disk should look like this:

    :::python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import os
    import sys
    import re
    import icecache  # Brad's API


    def parse(xyz_file):
        with open(xyz_file) as f:
            coords = re.findall(r"(-?[0-9\.]+)[\s\t\n]+", f.read())
        pos = [[float(coords[i]), float(coords[i + 1]), float(coords[i + 2])]
               for i in range(len(coords))[::3]]
        ic = icecache.icecache(len(pos))
        ic.addPointPosition(pos)
        ic.write("{}.icecache".format(os.path.splitext(xyz_file)[0]))

    if __name__ == "__main__":
        if len(sys.argv) == 2 and sys.argv[1].endswith(".xyz"):
            parse(sys.argv[1])
        else:
            raise Exception("Invalid file type")

Now, how cool is that? a simple regex plus 3 calls to Brad's API and
we're done.

Cheers!

[example]: http://softimage.wiki.softimage.com/index.php?title=Icecache_File_Format#Example_Cache_Writer_Python_Script
[api]: http://softimage.wiki.softimage.com/support/icecache.rar
[bunny]: http://coindesigner.sourceforge.net/data/bunny.991.xyz

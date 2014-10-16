Title: Speaking Maxscript
Author: Cesar Saez
Tags: 3dsmax, code, thoughts

Hi guys,

Today a friend asked for a quick way to create independent copies/instances
of an object at each vertex position of another mesh in 3dsmax.

I haven't worked with 3dsmax for a long time, but it seemed to be a job
for maxscript and she knows nothing about scripting, so I took a deep
breath and gave it a shot.

    for v in $[1].mesh.verts do (instance $[2]).pos = v.pos * $[1].transform

Here's the thing: maxscript turned out to be surprisingly straight forward,
I mean, this kind of stuff could be done in any DCC, but things like operator
overloading or grouping by parentheses really help to lower the
barrier and keep things simple.

Maxscript has some annoying parts for sure, but I have to admit it's a
lot simpler/easy-to-use than I remembered.

Cheers!
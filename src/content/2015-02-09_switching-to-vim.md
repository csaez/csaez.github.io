Title: Switching to VIM
Description: My experiences switching to VIM text editor.
Author: Cesar Saez
Tags: thoughts, code
Image: images/vim.png

Hi folks,

If you follow me on twitter you've probably noticed the tweets on my switch
from [sublime] to [vim].

I would like to share my experiences during the switching, the reasons behind
it and some of the advantages I see in my new daily workflow. 

### First things first

[Sublime Text][sublime] is a great code editor! I used it for the past 3~4
years without issues.  I love its `ctrl+shift+p` where all options are
accessible from the keyboard, I became addict to use multiple cursors and was
an early adopter of [package control][pc].

I also wrote my own snippets, build systems and all the things that you would
expect from a power user.

So, before get into why I switched and all that jazz, I would like to say that
[sublime] is a great code editor and you should definitely give it a try.

That said, let's talk about [vim]...

### Why switching?

All started by watching a [video on youtube][vyt], I never considered switching
or anything, it was plain and simple curiosity about this old, clunky and weird
editor.

I learned that it shouldn't look as ugly as with the default settings, modes
actually made sense (no more keyboard/mouse switching, yey!), there's an an
active community writing plugins and, most importantly, it's free and open
source.

"Interesting! but I won't switch just because of that" I thought... yeah,
right.

Since that day on, every time I had to grab the mouse to select or move around
some text, something inside me yells: _you are doing it wrong!_... and I
don't know you, but I used to grab the mouse to move around a lot!

So, a couple of weeks later I decided to give it a try.

### First impresions

In two words: _NO WAY_

There's _no way_ I could use this thing to develop anything on it. It's too
old, weird and ugly for me (yep, call me superficial, but the look is important
when you stare at it all day long).

So, what you do when this happen?

### Let's the tweaking begin!

I started by tweaking my `.vimrc` file adding syntax highlighting, a better
color scheme and all sort of small enhacements I probably stealed from the
internet.

Then I learned about plugins, so I installed [pathogen] to manage them and then
went to [ctrlp], [lightline], [python-mode], [snipmate] and [vim-surround].

And that was it...

> You can grab [my `.vimrc` from
> here](https://github.com/csaez/dotfiles/blob/master/.vimrc), it's fully
> commented and targeted to python development.

### Time to do some work

First days were a pain... forget about cool features, just moving around using
_hjkl_ keys instead of my beloved mouse/arrows-keys and switching between modes
was a challenge, not to talk about registers and the whole copy/paste thing.

But hey, after the initial shock things began to settle, I learned that hjkl
are not the most efficient moves to getting around text and the whole "command
nightmare" became a sort of continuous dialog with the editor (I'm not being
poetic here, commands work like verbs and can be combined in interesting
ways... you'll see).

To summarize: _indeed, I was doing it wrong_.

By the way, [this article][article] has helped me a lot.


### To this day...

I'm not an expert by any means, but I'm enjoying of some [vim] "super powers"
when coding... in fact, I would miss many features if I were forced to use
another editor.

I love the ability to run my code directly from vim (or any `bash` command),
`virtualenv` support is now essential to my workflow, I love not being forced
to jump between the keyboard and mouse to getting around text efficiently,
macros are great and I like the general approach to commands... even the look
and feel is nice once you tweak it!

And, of course, I'm very happy to be using open and free software.

## tl;dr

I switched to [vim] and I'm very happy with it (from a philosophical and
functional point of view).

Why should you consider it?

- It is free and open source software.
- Cross-platform, it's everywhere!
- Highly customizable.
- Efficient workflow.
- Config truly portable (1 file + plugins, no admin privileges needed).
- It's fun, you'll learn something new every day!

[sublime]: http://www.sublimetext.com
[vim]: http://www.vim.org
[pc]: https://packagecontrol.io/
[vyt]: https://www.youtube.com/watch?v=YhqsjUUHj6g
[pathogen]: https://github.com/tpope/vim-pathogen
[ctrlp]: https://github.com/kien/ctrlp.vim
[lightline]: https://github.com/itchyny/lightline.vim
[python-mode]: https://github.com/klen/python-mode
[snipmate]: https://github.com/garbas/vim-snipmate
[vim-surround]: https://github.com/tpope/vim-surround
[article]: http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/

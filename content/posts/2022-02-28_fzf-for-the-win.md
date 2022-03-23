---

title: FZF for the win!
description: If you spend any time in the terminal then you likely need to refer to things often by its name/path/identifier, in which case having the ability to select candidates via a fuzzy finder is a great addition to your toolbox!
date: 2022-02-28
categories: [Tutorials]
tags: [thoughts]
toc: false

---

<!--more-->

Hi there!

It has been a long time since the last time I posted something here.

A lot has happened: for starters I moved to London, got married, worked at DNEG for a while and
then switched to my current job in the research department (real time) at Foundry. My day to day
job is also a bit different, nowadays I find myself working on c++ projects developing prototypes
and/or experimental extensions to Foundry products.

Now, back to the topic... What's that `fzf` thingy I wanted to share about?

Well, I work a lot on the terminal (Linux) and during the years I have treasured quite a collection
of useful little tools to make my workflow nicer, one of them is FZF!

https://github.com/junegunn/fzf

`FZF` is an interactive Unix filter for command-line written in go, very handy to find files and
what not... The coolest part is how easy it is to integrate all sort of workflows into it, just
pipe the content to be filtered into `fzf` and you are ready to go!

## Executable launcher

A very useful thing I do a lot with `fzf` is to run a particular executable of the project I'm
working on (yes, there might be many executables on a given `cmake` project).

Here's a breakdown of how I have this setup:

### Finding executables

First we need to find all executables in the project, for that I do a recursive find starting on
the current directory (usually the root of the project) + a few greps further filtering things.

I usually create a `build` folder within the project containing the generated project out of
`cmake` where things get built, so this should cover that use case.

i.e. `~/bin/fx`

```bash
#!/bin/env bash
find . -type f -executable -exec file {} \; | grep -wE executable | grep -Po ".*(?=:)"
```

### Selecting the executable in `fzf`

Now we can simply pipe the results into `fzf` in order to filter the results and launch the
executable!

In my case I change directory to the executable directory and run it from there, I do this because
I work on projects that need to run on multiple platforms and there's a bit of cross platform
`rpath` "fun" involved leading to this decision :see_no_evil:.

i.e. `~/bin/xx`

```bash
#!/bin/env bash
result=$( fx | fzf )
if [[ -z $result ]]; then
  exit 0
fi
pushd $(dirname $result) > /dev/null
./$(basename $result)
```

We are done! Simply type `xx` on your terminal and enjoy your fancy selector to launch executables
within your project!

### Wait, what about debugging?

Right, you can do the same thing to launch your application under a debugger (`gdb` in this case).

i.e. `~/bin/dd`
```bash
#!/bin/env bash
result=$( fx | fzf )
if [[ -z $result ]]; then
  exit 0
fi
pushd $(dirname $result) > /dev/null
gdb ./$(basename $result)
```

### What about doing this from the IDE/code-editor?

I use `neovim` as my code editor, one of the cool things is the tight integration with the terminal
allowing to reuse some of the little scripts we have been talking about. Here's my setup (using the
`fzf` plugin for the case of debugging).

```lua
local noremap = { noremap=true, silent=true }

-- launch debugger using termdebug (i.e. set breakpoints in the editor)
vim.cmd [[:packadd termdebug]]
vim.g.termdebug_wide = 1
vim.api.nvim_set_keymap('n', '<Leader>dd', [[ :call fzf#run(fzf#wrap({'source': 'fx', 'sink': 'Termdebug'}))<CR>]], noremap)

-- launch executable in new tab (terminal buffer, non-blocking)
vim.api.nvim_set_keymap('n', '<Leader>xx', [[ :tabe | term xx<CR> ]], noremap)
```

Whaaaaat!? Exactly! :exploding_head:

---

Regardless of this particular setup, I think the beauty of it is on the simple interface, allowing
to quickly create all sorts of throw away scripts adding a fancy selector to all sort of things
(i.e. Do you want to pimp up your git workflow? Take a look at how
[forgit](https://github.com/wfxr/forgit) uses `fzf` for inspiration).


Cheers!

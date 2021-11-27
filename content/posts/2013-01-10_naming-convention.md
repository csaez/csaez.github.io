---

title: "Handling naming conventions"
description: Thoughts around naming conventions during the development of RigLab
date: 2013-01-10
categories: []
tags: [thoughts, pipeline]

---
<!--more-->
Hey folks,

I've been working on the naming convention side of the rigging framework
and I wanna share my take on this problem.

I know, this isn't the hottest subject to talk about, but as it's a so
general problem I thought could be interesting for you too.

## First of all: a disclaimer...

A lot of things I'm developing for this project are influenced by the
way I'm used to work. I'm not trying to steal ideas from anyone, it's
inevitable carry with me some concepts that I found interesting and make
them mine.

Thanks to all who shared their thoughts on pipeline/coding with me along
the years. Lots of inspiration comes from those talks!

## What's a naming convention?

As you may know, a naming convention is just an agreement about the
information and the format we will be using to define a name.

### So, what's the big deal?

Well, let me break things up a little bit...

*On the user side* it's just a convention and we are clever
enough to remember it, so it's completely up to the user assign names
properly. Some studios provide sophisticated tools to help them on the
task, but in my experience a simple renamer tool (string operations)
with some batch capabilities is enough in most cases.

*On the code side* it's a completely different story,
code/software is not smart enough to figure out a naming convention so
we have to be very explicit about it.

One way to tackle the problem is just hard-coding names, we all have been
there at some point. It just works, but turns out to be a really bad
idea in the long run.

The conventions usually evolve/change between projects/clients, if you
hard-code things then all your tools become useless unless you revisit
the code and change everything name related.

The other way is create a layer to solve the names using the conventions
and work with those names on your code, this way you have a centralized
place where set the new naming requirements and all your tools becomes
name independent.

I obviously recommend the second approach.

### What has been done in the framework?

If we go back to the [project goals][1], there is a specific one about
naming convention, let me quote it.

> The system will be based on metadata rather than any specific naming
> convention. The naming convention will be based on a configuration file in
> order to integrate the system on any pipeline (the same is true with
> colours, animation controls and all the standard rigging conventions).

At first I worked in a metadata API to store everything, but as the
project progresses, I realized that access metadata is not user-friendly
at all and it would be very difficult to trust the data if it's not
updated by the user... And the system must assign a name to new objects
anyway!

So in an unexpected turns of events, I still use metadata to store
specific things but I also worked on a system that allows me use the
data stored in the naming convention (which are much more likely to be
updated by the user).

A cool thing about the new manager is that ended up being software
agnostic, so it can be used in mixed pipelines too.

You can see how it works in the video below.

{{< vimeo 57161770 >}}

## API Design

When it comes to naming convention is really difficult design an
easy-to-use API, it's difficult because we have to specify every 'token'
value but at the same time we shouldn't be typing any longer than the
name itself.

In my experience if you're working with a too intricate API, the
temptation to hard-code names tend to be too high (especially in
scripting) and the whole system becomes meaningless.

Here are a couple of simple concepts that helped me to create an easy to
use design.

### Manager

_If you don't want to be too explicit you are probably looking for a way
to share 'global' information, in my case I decided to work with a
manager as a layer for the 'naming resolution' stuff instead of just at
a module level, this way I can work with some 'global' values instead of
specified them each time._

### Active Rule

_The manager expect an active rule to work with, you can set/get the
active rule at anytime. Using this way to deal with rules allow us be a
lot less explicit on each name solving and let the manager do some
clever stuff to figure out how to arrange the name using the incoming
arguments._

### Overrides

_We can override default values at a manager level at any time, this
becomes really handy when you're working on the same context and don't
want to be explicit about every token on every name._

I hope this make sense,

Cheers!

[1]: http://csaez.blogspot.com/2012/11/csriglab-overview.html

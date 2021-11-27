---

title: "Introducing RigLab"
description: I'm embarking o a new adventure developing an open source rigging framework.
date: 2012-11-13
categories: []
tags: [thoughts, rigging]

---
<!--more-->
I'm finally working on my rigging framework, I've been thinking about it
for a long time and I finally have a clear picture of what I want as end
result... and even more important, why I want it that way!

There will be plenty of new problems to be sorted out as I go with the
development, but the overall design and workflows are clear on my mind
now.

## So, why a framework?

I've already written 3 autorigs for different productions, 2 of them for
3dsmax (advertising projects and a TV series) and the latest one for
softimage (feature film)... The "autorig philosophy" allow us to work
faster and helps to standarize things, but at the end it's not enough.

If you limit yourself to make a rig-builder/autorig, at some point it
will be obvious that you're leaving a lot behind, the solution tend to
be specific to the nature of the asset (bipeds, quadrupeds and so on)
and sometimes it's difficult to update/expand it without refactoring the
system. So we end up creating new autorigs to cover unexpected
requirements (props, vehicles, environments, facial rigs, whatever)
rather than unify and keep them under the same roof.

A framework lives in a much more general level and represents that roof,
describes the way you manage/work-with rigs. The autorigs (I call them
solvers) are built on top, so you always have control over your rigs no
matter how they were built (including by hand).

## Goals

In order to get this done in a reasonable time frame I've to set some
goals for the project, the following list represent the main ones (in
arbitrary order).

### Metadata

The system will be based on metadata rather than any specific naming
convention. The naming convention will be based on a config file in
order to integrate the system on any pipeline (the same is true with
colours, animation controls and all the standard rigging conventions).

### Multipose support

The framework should allow us to define a rigging pose (by default will
be the same as the binding pose). This is important because the binding
pose isn't always the best for rigging/animation purposes (nonorthogonal
limbs and stuff like that).

### Macro support for solver authoring

This is HUGE! When you're on production and there's a need for a new
kind of rigging solution, code it and update the rigging system isn't
the fastest solution (sometimes it's not even possible). Support a sort
of macro to facilitate the solver's creation will help to keep the
rigging system alive and updated.

### Non-linear workflow

The rigging process is an iterative one, the system should allow us go
back to the creation state for editing/updating. A rig is never really
finished and we need a bidirectional way to work with them.

### Robust API

From my point of view the system has 2 clients: the gui (graphic user
interface) and another programs/tools, the system should be able to work
with both (this include batch processing).

## Current status

The overall design and the workflow are finished (I'm still documenting,
but I have a clear picture of how everything should work). Right now I'm
working on the metadata manager and starting the multipose part.

There're a lot of work to do in order to get it up and running, but this
time I really want to materialize these ideas into something useful, I
will be working actively in the coming months to complete the project as
soon as possible.

Hope to have something interesting to show in the next post, we'll see
:wink:

Cheers!

Title: The Lego Journey
Description: It's a wrap! The Lego Batman Movie is out and Ninjago on its way, time for a retrospective.
Author: Cesar Saez
Tags: works, thoughts, recommended
Image: images/lego-batman.png

Hi folks,

It has been a while since I was involved on the making of these films, but now that _Lego Batman_ is
out and _Ninjago_ is on its way I would like to share some sort of retrospective of my journey around
these projects.

If you are not familiar with the LEGO movies here are the mandatory trailers.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/rGQUKzSDhrg?rel=0" frameborder="0" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/sZSYYiATFTI?rel=0&amp;start=10" frameborder="0"
allowfullscreen></iframe>

My hope after writing this is to hopefully bring some light to people starting their careers or
maybe that haven't had the opportunity to work on these types of projects yet. I clearly remember
my young self being inspired by reading interviews of artists working on movies while living in
Chile where all this seems so out of reach. But you know what... somehow I'm here! and maybe some
of the lessons I've learned during my bumpy journey can help you too.

## Joining Animal Logic

I still remember my first day very vividly, I was quite excited about the opportunity to work at
_AL_, I've had the chance to work on animated tv series and actually supervised an animated movie
before joining AL, but it was clearly a step up for me. On top of that there was the whole
Australian experience and living in an English speaking country for the first time... There was a
lot going on.

My first day I met 2 new starters for the rigging department, we had some generic induction
sessions and later on we were introduced to the team and left at our desks doing mostly paperwork
and looking around the wiki. Eventually we got a few sessions with our supervisor explaining how
things work, it was a lot to take in a few hours.

Later I learned first hand that training new starters is not an easy task, there's a lot built over
the years and it's easy to take things for granted after being around for some time, more on this
later.

Anyway, back to training, I think being a group made the experience much easier as we all
shared our notes and helped each other trying to figure out things without having to bother other
people too often. It might sound silly, but the team spirit was there since day one making the
experience a breeze.

This lead me to the first piece of advice:

> Make an effort to get along with your peers, have lunch together! teams are more than just
> workers sharing a project. Start building a network around you as soon as you can, it's hands
> down the cheapest and more effective investment you can do for your career and your well being.

In my case I had the whole language barrier going on, it was pretty tough to even understand what
people was talking about at the table. But after a while I figured that instead of fighting this or
use it as an excuse, I could totally take advantage of it! This barrier was precisely what made me
different and interesting to people, I realized that instead of struggling with it I could use it
as a chat opener, people love to learn about different cultures, languages and anything really! we
come from different sides of the world, sometimes from very different realities, and sharing those
perspectives makes an interesting discussion, even if it implies everybody having to make an effort
to understand each other. Having great teammates helps a lot (if anyone is reading, thanks!).

## Looking with fresh eyes

An interesting thing about working on _LEGO_ movies at _Animal Logic_ is that we really strive to stay
true to the medium, nothing deforms in ways that cannot be done with the real toys, actually
there's a strong correlation between the digital assets and the _LEGO_ catalogue, so cheating to make
things look cool is not really an option (anim uses a ton of per-frame brick replacement).
This imposes a lot of constraints to animation and rigging, making it an interesting challenge. I
certainly wasn't expecting to work on such complex mechanical rigs and procedural face systems.

Pipeline/technology wise though, the first _LEGO_ movie paved the way for the next ones, the pipeline
was quite stable and we didn't need to reinvent too many wheels... in theory.

Working with old-ish pipelines while pushing the envelope in terms of complexity/scale has its
downsides, for instance rigging for the _LEGO_ movies was 100% code-based (other than adjusting
guides) and the framework in which the rigs were defined had some room for improvement. After a few
months learning the system I decided to write a few pages of feedback (+ possible solutions) and
after clear it out with some trusted peers I sent it over to my supervisor.

Surprisingly he was very open to my feedback and that leaded to getting involved doing very
significant changes to the way builders and components communicated with each other simplifying
asset scripts and the overall design of the system a lot. We moved from what I call _"class
oriented programming"_ (I've [written a bit about it in the
past](http://www.cesarsaez.me/2015/09/stop-cop.html)) to more generic entities reducing the amount
and complexity of code dramatically. I also develop a few key components dealing with spline-ish
elements and did a lot of work on the procedural face system (on top of in-house software, a very
unique experience).

And this leads us to the second piece of advice:

> Never underestimate the power of fresh eyes! A lot of times people start accepting whatever they
> have as the way things works (tm), that opens a huge opportunity to bring blind spots to the
> table and help improving things. Your perspective is one of your best weapons!

This is not to say that you will get there and change everything, you obviously need to learn the
current system and understand why things are the way they are (pleae don't assume the previous guy
wasn't as clever as you think you are, that's not as reality works)... But past certain point
there's the possibility that you might see some blind spot and depending on the team and production
you might get a chance to get involved doing very interesting work.

This could not happened without the trust of my supervisor at the time: _Josh Murtack_. He gave me
a lot of room to dig deeper into the system and discuss different ideas around how to improve the
overall design. What was even more impressive to me was his attitude towards my suggestions,
allowing me to develop prototypes even in cases where he didn't fully saw where I was trying to go
with the system (take into account the language barrier). I _really_ appreciate his support during
my time working on _LEGO_ movies, he's one of the best supervisors I've ever worked with.

## New opportunities

After a year working in the rigging department, and perhaps because of my work and interest
refactoring the _LEGO_ rigging system, I had the opportunity to get involved in the making of the
new rigging technology at the _Performance Technology Group_ (a small group inbetween rigging and
RnD).  This meant I finally made the switch to a software developer position (yay!).

Since then I've been working as part of _Raffaele Fragapane_ team re-inventing the way we do rigging
across the facility, starting from first principles with a strong focus on performance. My work
here has been a lot more technical and I cannot go into details because of NDA, but I'm very happy
with what we have built so far and hopefully you will be able to see some of the projects making
use of this technology very soon.

I have no doubts I've been very lucky to even have these opportunities, but leaving the luck
factor aside, the take away here is:

> Your actions will somehow get reflected in your future, sometimes is not obvious, sometimes is very
> straight forwards, but it happen. So my advice here is to focus in the present as it's your only
> way to model the future, everything else will come as a consequence. Lead by example, do _the
> right thing_ (whatever that means to you) no matter your surroundings/circumstances and you will
> increase the chances to reach your goals.

From a more personal point of view, I've been taking some time to learn about more technical
domains, I actually took a class on _functional programming_ last year and have been getting more
familiar with low level code and how hardware really works. I still do plenty of _python_
development though, but I switch to _C/C++_ when I have a chance and I've been playing quite a bit
with different languages in my spare time (_Rust_ ftw!... more seriously, there are a lot of great
ideas being implemented in new-ish languages).

## The present.

I've been at _AL_ for two and a half years now, it has been an incredible journey so far and I'm very
grateful for the chance to be around here. Next month I'm moving again, this time to the _RnD_
department taking on even bigger challenges under a new team.

I'm kinda glad to move away from rigging, it's an interesting topic but after 10 years tinkering
around it I'm pretty sure being outside of my comfort zone will push me to grow in new
directions, there will be ups and downs but I'm willing to do my best.

And that leads us to the end... it's a wall of text! I know, but I sincerely hope some of my stupid
advices and experience encourage newcomers to enjoy their journey and go for their goals.

Cheers!

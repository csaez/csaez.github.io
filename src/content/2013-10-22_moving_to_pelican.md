Title: Moving to pelican
Author: Cesar Saez
Tags: thoughts

I did it! I finally switched to a 'static' site :)

## Why?

To be honest I was bored of the 'blogging platforms' overhead.

For simple use cases there's the good ol' [blogger][b], it works fine
and it's quite secure but has some serious limitations on the customization
side and its templates are extremely messy (all in one big xml file).

So, if you want to go custom the obvious choice seems to be [wordpress][wp],
I've used it for a while and it works well, but it requires a hell of
maintenance in order to stay away of security problems... I thought 'nobody
would like to hack a personal blog' and there you go, I was hacked twice.
I think there are so many sites running on top of wordpress that it's not
that improbable get randomly hacked because of a new vulnerability.

At the end I just wanted a simple blogging platform (no need for e-commerce
or any fancy feature, just blogging), secure and easy to use... it seems a
perfect use case for a static site generator :)

[b]: http://www.blogger.com
[wp]: http://www.wordpress.org

### How does it works?

You write your posts as text files using a simple markup lenguague
(markdown, ReST, YAML) and the generator parse the content and rebuild
the entire site for you.

The output is static site but as you can rebuild the entire thing in no
time it works perfectly on personal sites like this one.

### What about comments?

Yep, comments are dynamic by nature so the only way to implement them on
a static sites is via external services + some javascript.

I was using google+ comments on [blogger][b] and I could implement them
here too, but they are too attached to google plus and I prefered use a
less intrusive service like [disqus][d].

[d]: http://disqus.com/

### What about publishing?

Upload the entire site each time I write or edit something could be
annoying, but *there is the cloud!*

There are many cloud services that could be handy on this one, a quick
search lead us to people hosting their sites via [dropbox][db],
[github][gh], [heroku][heroku] and many many others.

Since I'm already using [git][git] and [github][gh] for my open source
projects I decided to add this site too, perhaps it's not the
best solution from a CEO point of view but I really don't care too much
about that and [github pages][gh-pages] makes it almost
efortless, I just push the generated output to a specific branch and
github serves the latest version.

[db]: http://www.dropbox.com
[gh]: http://www.github.com
[heroku]: http://www.heroku.com
[git]: http://www.git-scm.com
[gh-pages]: http://pages.github.com/

### Why pelican?

I was really tempted by [jekyll][j] but it's written in [ruby][ruby]
and I'm not familiar with the language, so I ended up looking for a
[python][py] based one and [pelican][p] seemed to be quite popular
([nikola][n] looked promising too).

[j]: http://www.jekyllrb.com
[ruby]: http://www.ruby-lang.org
[p]: http://pelican.readthedocs.org
[py]: http://www.python.org
[n]: http://www.getnikola.com

## Migrating

Migrate implied export the blog posts to markdown and tweak the templates,
it tooks some time but wasn't that difficult.

#### Posts to markdown:

I love the idea of start using [markdown][md] as writing formating for my
posts, it's easy to the eyes and fits nicely with the 'separation of
conserns' filosophy.

Pelican offers some automatic migration tools, I tried converting the rss
feed to markdown and it 'worked' but just as a base, I ended up tweaking
all markdown files by hand. Fortunatelly (?) I didn't have much articles
on blogger (remember those wordpress hack attacks? yep...) and wasn't that
painfull.

[md]: http://daringfireball.net/projects/markdown/

#### Templates:

Pelican uses [jinja2][j2] as template engine, the templates are a bit low
level compared with Jekyll's ones but they are much more powerfull and, as
jinja is python based, you can pass all kind of metadata between
pages/articles/config files.

I also wanted to redesign the site and somehow update my 'webdev skills',
last time I built a website was using macromedia dreamweaver 10 years ago
(you know, hardcoded tables everywhere and all kind of webdev atrocities).

[j2]: http://jinja.pocoo.org

### tl;dr

I finally migrated to a static site that can be customized, it is secure,
open source and that I understand (no black boxes here).

I honestly don't think this is the right move for everyone, but if you are
somewhat technical it's well worth it.

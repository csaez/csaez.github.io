#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Cesar Saez"
SITENAME = u"CESAR SAEZ"
SITESUBTITLE = u"Character Technical Director"
SITEURL = "http://www.cesarsaez.me"
DISQUS_SITENAME = "csaez"
GOOGLE_ANALYTICS = "UA-45090469-1"
GOOGLE_ANALYTICS_NAME = "cesarsaez.me"

DEFAULT_LANG = "en"
LOCALE = ("usa", "jpn", "en_US", "ja_JP")

TIMEZONE = "America/Santiago"
DEFAULT_DATE_FORMAT = u"%B %d, %Y"

MENUITEMS = (("Contact", "mailto:cesarte@gmail.com"), )
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = "Blog"

SUMMARY_MAX_LENGTH = 120

PATH = "src/content"
THEME = "src/theme/custom-bootstrap"

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None

FILENAME_METADATA = "(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
]

PLUGIN_PATH = "src/pelican-plugins/"
PLUGINS = ("liquid_tags.img", "liquid_tags.video",)

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}.html"
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"
PAGE_LANG_URL = "pages/{slug}-{lang}.html"
PAGE_LANG_SAVE_AS = "pages/{slug}-{lang}.html"

ARCHIVES_SAVE_AS = False
AUTHOR_URL = False
AUTHOR_SAVE_AS = False
AUTHORS_URL = False
AUTHORS_SAVE_AS = False

DIRECT_TEMPLATES = ("index", "tags", "categories", "archives")
PAGINATED_DIRECT_TEMPLATES = ("index",)

# Social widget
SOCIAL = (("Google+", "http://www.google.com/+CesarSaez"),
          ("Twitter", "http://twitter.com/csaezmargotta"),
          ("Linked in", "http://www.linkedin.com/in/cesarsaez"),
          ("Github", "http://www.github.com/csaez"),
          ("Vimeo", "http://www.vimeo.com/csaez"),
          ("Feed", "http://feeds2.feedburner.com/csaez"),)

SOCIAL_CLASSES = ("fa fa-google-plus",
                  "fa fa-twitter",
                  "fa fa-linkedin",
                  "fa fa-github",
                  "fa fa-vimeo-square",
                  "fa fa-rss")

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DEFAULT_PAGINATION = 10

DELETE_OUTPUT_DIRECTORY = True
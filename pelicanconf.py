#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cesar Saez'
SITENAME = u'CESAR SAEZ'
SITESUBTITLE = u'Character TD'
EMAIL = u'hi@cesarsaez.me'
SITEURL = ''

PATH = 'src/content'
THEME = 'src/theme/csaez-simple'
STATIC_PATHS = ['images',
                'extra/.htaccess',
                'extra/CNAME',
                'extra/browserconfig.xml',
                'extra/apple-touch-icon.png',
                'extra/apple-touch-icon-57x57.png',
                'extra/apple-touch-icon-60x60.png',
                'extra/apple-touch-icon-72x72.png',
                'extra/apple-touch-icon-76x76.png',
                'extra/apple-touch-icon-114x114.png',
                'extra/apple-touch-icon-120x120.png',
                'extra/apple-touch-icon-144x144.png',
                'extra/apple-touch-icon-152x152.png',
                'extra/apple-touch-icon-180x180.png',
                'extra/apple-touch-icon-precomposed.png',
                'extra/favicon.ico',
                'extra/favicon-16x16.png',
                'extra/favicon-32x32.png',
                'extra/favicon-96x96.png',
                'extra/favicon-160x160.png',
                'extra/favicon-192x192.png',
                'extra/mstile-70x70.png',
                'extra/mstile-144x144.png',
                'extra/mstile-150x150.png',
                'extra/mstile-310x150.png',
                'extra/mstile-310x310.png']
EXTRA_PATH_METADATA = {
    'extra/.htaccess': {'path': '.htaccess'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/apple-touch-icon-57x57.png': {'path': 'apple-touch-icon-57x57.png'},
    'extra/apple-touch-icon-60x60.png': {'path': 'apple-touch-icon-60x60.png'},
    'extra/apple-touch-icon-72x72.png': {'path': 'apple-touch-icon-72x72.png'},
    'extra/apple-touch-icon-76x76.png': {'path': 'apple-touch-icon-76x76.png'},
    'extra/apple-touch-icon-114x114.png': {'path': 'apple-touch-icon-114x114.png'},
    'extra/apple-touch-icon-120x120.png': {'path': 'apple-touch-icon-120x120.png'},
    'extra/apple-touch-icon-144x144.png': {'path': 'apple-touch-icon-144x144.png'},
    'extra/apple-touch-icon-152x152.png': {'path': 'apple-touch-icon-152x152.png'},
    'extra/apple-touch-icon-180x180.png': {'path': 'apple-touch-icon-180x180.png'},
    'extra/apple-touch-icon-precomposed.png': {'path': 'apple-touch-icon-precomposed.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    'extra/favicon-160x160.png': {'path': 'favicon-160x160.png'},
    'extra/favicon-192x192.png': {'path': 'favicon-192x192.png'},
    'extra/mstile-70x70.png': {'path': 'mstile-70x70.png'},
    'extra/mstile-144x144.png': {'path': 'mstile-144x144.png'},
    'extra/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extra/mstile-310x150.png': {'path': 'mstile-310x150.png'},
    'extra/mstile-310x310.png': {'path': 'mstile-310x310.png'},
    }

TIMEZONE = 'America/Santiago'
DEFAULT_DATE_FORMAT = u"%d %b %Y"

DEFAULT_LANG = u'en'
LOCALE = ("usa", "en_US.UTF-8")

FILENAME_METADATA = "(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}.html"
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"
PAGE_LANG_URL = "pages/{slug}-{lang}.html"
PAGE_LANG_SAVE_AS = "pages/{slug}-{lang}.html"

AUTHOR_URL = False
AUTHOR_SAVE_AS = False
AUTHORS_URL = False
AUTHORS_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
  ("github", "http://www.github.com/csaez"),
  ("google", "http://plus.google.com/+CesarSaez"),
  ("linkedin", "http://www.linkedin.com/in/cesarsaez"),
  ("twitter", "http://twitter.com/csaezmargotta"),
  ("vimeo", "http://www.vimeo.com/csaez")
)

ICONS = {
    "archive": r'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" width="512" height="512" viewBox="0 0 512 512" xml:space="preserve" enable-background="new 0 0 512 512"><path d="M444.8 259v203h-378V259h40v163h298V259H444.8zM297.8 320h-83.9c-9.7 0-17.5-7.8-17.5-17.5 0-9.7 7.8-17.5 17.5-17.5h83.9c9.7 0 17.5 7.8 17.5 17.5C315.3 312.2 307.4 320 297.8 320zM461.8 132v97H50.2v-97l76.6-82h259L461.8 132zM112.7 123.7h286.8L368.3 90H144.2L112.7 123.7zM421.8 189v-25.3H90.2V189H421.8z"/></svg>',
    "home": r'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" width="512" height="512" viewBox="0 0 512 512" enable-background="new 0 0 512 512" xml:space="preserve"><path d="M419.5 275.8v166.2H300.7v-90.3h-89.5v90.3H92.5V275.8H50L256 70l206 205.8H419.5zM394.1 88.5h-47.9v38.3l47.9 48V88.5z"/></svg>',
    "github": r'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" width="512" height="512" viewBox="0 0 512 512" xml:space="preserve" enable-background="new 0 0 512 512"><path d="M412 50H100c-27.6 0-50 22.4-50 50v312c0 27.6 22.4 50 50 50h312c27.6 0 50-22.4 50-50V100C462 72.4 439.6 50 412 50zM301.7 396.4c-7.3 1.4-9.6-3.1-9.6-6.9 0-4.7 0-20.3 0-39.6 0-13.4-4.7-22.2-9.9-26.7 32.1-3.6 65.8-15.8 65.8-71.1 0-15.7-5.6-28.6-14.8-38.7 1.5-3.6 6.4-18.3-1.4-38.2 0 0-12.1-3.9-39.6 14.8 -11.5-3.2-23.9-4.8-36.1-4.9 -12.3 0.1-24.6 1.7-36.1 4.9 -27.6-18.7-39.7-14.8-39.7-14.8 -7.8 19.9-2.9 34.5-1.4 38.2 -9.2 10.1-14.9 23-14.9 38.7 0 55.3 33.7 67.6 65.7 71.3 -4.1 3.6-7.9 10-9.2 19.3 -8.2 3.7-29.1 10.1-42-12 0 0-7.6-13.8-22.1-14.9 0 0-14.1-0.2-1 8.8 0 0 9.5 4.4 16 21.1 0 0 8.4 25.7 48.5 17v26.9c0 3.8-2.3 8.3-9.5 6.9 -57.3-19.1-98.6-73.1-98.6-136.8 0-79.6 64.6-144.2 144.2-144.2 79.6 0 144.2 64.6 144.2 144.2C400.2 323.3 358.9 377.3 301.7 396.4z"/></svg>',
    "google": r'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" width="512" height="512" viewBox="0 0 512 512" enable-background="new 0 0 512 512" xml:space="preserve"><path d="M209 235.7c-22.3-0.7-43.6-21.2-47.4-50.5 -3.9-29.3 11.1-51.8 33.5-51.1 22.3 0.7 41.4 24.7 45.3 54.1C244.2 217.5 231.4 236.3 209 235.7zM204.5 295.7c-33.3-0.4-61.5 21-61.5 45.8 0 25.3 24 46.4 57.3 46.4 42.5 0 63.1-19.8 63.1-45.1C263.4 318.7 241.4 295.7 204.5 295.7zM461.9 101v312c0 27.6-22.4 50-50 50h-312c-27.6 0-50-22.4-50-50V101c0-27.6 22.4-50 50-50h312C439.6 51 461.9 73.4 461.9 101zM292.1 339.9c0-23.4-8.7-38.6-35.1-58.4 -26.8-19.5-33.3-30.6-7.8-50.3 14.4-11.1 24.5-26 24.5-44.3 0-20-8.2-38.1-23.5-46.9h21.8l18.5-19.4c0 0-69.8 0-82.9 0 -51.7 0-77.1 31-77.1 65.1 0 34.9 23.9 62.3 70.6 62.3 -7.2 14.6-4.3 28.1 7.5 37.8 -79.8 0-96.8 35-96.8 62 0 34.9 40.2 55.7 88.3 55.7C265.9 403.4 292.1 368.5 292.1 339.9zM400.1 162.6H361.9v-38.2h-19.1v38.2h-38.2v19.1h38.2v38.2h19.1v-38.2h38.2V162.6z"/></svg>',
    "linkedin": r'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" width="512" height="512" viewBox="0 0 512 512" enable-background="new 0 0 512 512" xml:space="preserve"><path d="M411.9 50h-312c-27.6 0-50 22.4-50 50v312c0 27.6 22.4 50 50 50h312c27.6 0 50-22.4 50-50V100C461.9 72.4 439.6 50 411.9 50zM181 393h-56.5V210.3h56.5V393zM152.5 186.4c-18.5 0-33.4-15.1-33.4-33.7 0-18.6 15-33.7 33.4-33.7 18.5 0 33.4 15.1 33.4 33.7C185.9 171.3 170.9 186.4 152.5 186.4zM392.9 393h-56.3c0 0 0-69.6 0-95.9 0-26.3-10-41-30.8-41 -22.6 0-34.5 15.3-34.5 41 0 28.1 0 95.9 0 95.9h-54.2V210.3h54.2v24.6c0 0 16.3-30.2 55-30.2s66.5 23.6 66.5 72.6C392.9 326.3 392.9 393 392.9 393z"/></svg>',
    "twitter": r'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" width="512" height="512" viewBox="0 0 512 512" enable-background="new 0 0 512 512" xml:space="preserve"><path d="M412 50H100c-27.6 0-50 22.4-50 50v312c0 27.6 22.4 50 50 50h312c27.6 0 50-22.4 50-50V100C462 72.4 439.6 50 412 50zM371.9 207.1c3.6 79.1-55.4 167.2-159.8 167.2 -31.7 0-61.3-9.3-86.2-25.3 29.8 3.5 59.6-4.8 83.2-23.3 -24.6-0.5-45.4-16.7-52.5-39 8.8 1.7 17.5 1.2 25.4-1 -27-5.4-45.7-29.8-45.1-55.8 7.6 4.2 16.2 6.7 25.5 7 -25-16.7-32.1-49.8-17.4-75 27.7 34 69.1 56.4 115.9 58.7 -8.2-35.2 18.5-69 54.8-69 16.2 0 30.8 6.8 41 17.8 12.8-2.5 24.8-7.2 35.7-13.6 -4.2 13.1-13.1 24.1-24.7 31.1 11.4-1.4 22.2-4.4 32.3-8.9C392.5 189.3 382.9 199.2 371.9 207.1z"/></svg>',
    "vimeo": r'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0" y="0" width="512" height="512" viewBox="0 0 512 512" enable-background="new 0 0 512 512" xml:space="preserve"><path d="M412 50H100c-27.6 0-50 22.4-50 50v312c0 27.6 22.4 50 50 50h312c27.6 0 50-22.4 50-50V100C462 72.4 439.6 50 412 50zM399.1 192c-1.3 28.1-20.9 66.5-58.8 115.3 -39.2 51-72.4 76.5-99.5 76.5 -16.8 0-31-15.5-42.7-46.6 -7.8-28.5-15.5-56.9-23.3-85.4 -8.6-31-17.9-46.6-27.8-46.6 -2.2 0-9.7 4.5-22.6 13.6l-13.6-17.5c14.2-12.5 28.3-25 42.1-37.5 19-16.4 33.2-25 42.7-25.9 22.4-2.2 36.3 13.2 41.4 46 5.6 35.4 9.5 57.5 11.7 66.1 6.5 29.4 13.6 44.1 21.4 44.1 6 0 15.1-9.5 27.2-28.6 12.1-19.1 18.5-33.6 19.4-43.6 1.7-16.5-4.8-24.7-19.4-24.7 -6.9 0-14 1.6-21.3 4.7 14.2-46.4 41.3-69 81.2-67.7C386.8 135.1 400.8 154.4 399.1 192z"/></svg>',
}

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

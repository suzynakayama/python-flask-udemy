"""
libs.strings

By default, uses `en-us.json` file inside the `strings` top-level folder.

If language changes, set `libs.strings.default_locale` and run `libs.strings.refresh()`

Works in a very similar way as Babel
"""

import json

default_locale = "en-us"

cached_string = {}

def refresh():
    global cached_strings
    with open(f"strings/{default_locale}.json") as f:
        cached_strings = json.load(f)  # json.load() will load all content from the strings/default_locale.json file and return as a dictionary

def gettext(name):
    return cached_string[name]

def set_default_locale(locale):
    global default_locale
    default_locale = locale

refresh()
# -*- coding: utf-8 -*-

"""
requests.compat
~~~~~~~~~~~~~~~

This module handles import compatibility issues between Python 2 and
Python 3.
"""

import chardet          # Python2/3 compatible character encoding detector

import sys

# -------
# Pythons
# -------

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

# json is simplejson, added to the stdlib, But since json was added in 2.6, simplejson has the advantage of working on more Python version(2.4+)
# simplejson is also updated more frequently than Python, so if you need (or want) the latest version, it's best to use simplejson itself.
try:
    import simplejson as json
except ImportError:
    import json

# ---------
# Specifics
# ---------

if is_py2:
    from urllib import (
        quote, unquote, quote_plus, unquote_plus, urlencode, getproxies,
        proxy_bypass, proxy_bypass_environment, getproxies_environment)
    from urlparse import urlparse, urlunparse, urljoin, urlsplit, urldefrag
    from urllib2 import parse_http_list
    import cookielib
    from Cookie import Morsel
    from StringIO import StringIO

    from urllib3.packages.ordered_dict import OrderedDict

    builtin_str = str
    bytes = str
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)
    integer_types = (int, long)

elif is_py3:
    from urllib.parse import urlparse       # Parse a URL into six components, returning a 6-tuple[scheme, netloc, path, params, query, fragment]
    from urllib.parse import urlunparse     # Construct a URL from a tuple as returned by urlparse()
    from urllib.parse import urlsplit       # similar to urlparse(), but does not split the params from the URL
    from urllib.parse import urlencode      #
    from urllib.parse import quote          # Replace special characters in string using the %xx escape.
    from urllib.parse import unquote        # Replace %xx escapes by their single-character equivalent
    from urllib.parse import quote_plus, unquote_plus, urldefrag
    from urllib.request import parse_http_list, getproxies, proxy_bypass, proxy_bypass_environment, getproxies_environment
    from http import cookiejar as cookielib
    from http.cookies import Morsel         # Abstract a key/value pair
    from io import StringIO                 # An in-memory stream for text I/O
    from collections import OrderedDict

    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float)
    integer_types = (int,)

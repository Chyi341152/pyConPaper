"""Module containing bug report helper(s)."""
from __future__ import print_function

import json         # JSON encoder and decoder
import platform     # Access to underlying playform's identifying data
import sys
import ssl          # TLS/SSL wrapper for socket objects

import idna         # Internationalized Domain Names in Application(IDNA)
import urllib3
import chardet

import os,sys

#from requests import __version__ as requests_version
import __version__ as requests_version             # my change


# try ... except statement has an optional else clause,It is useful for code that must be executed if they try clause does not raise an exception.
try:
    from urllib3.contrib import pyopenssl
except ImportError:
    pyopenssl = None
    OpenSSL = None
    cryptography = None
else:
    import OpenSSL
    import cryptography


def _implementation():
    """Return a dict with the Python implementation and version.

    Provide both the name and the version of the Python implementation
    currently running. For example, on CPython 2.7.5 it will return
    {'name': 'CPython', 'version': '2.7.5'}.

    This function works best on CPython and PyPy: in particular, it probably
    doesn't work for Jython or IronPython. Future investigation should be done
    to work out the correct shape of the code for those platforms.
    """
    implementation = platform.python_implementation()           # Returns a string identifying the Python implementation.

    if implementation == 'CPython':
        implementation_version = platform.python_version()
    elif implementation == 'PyPy':
        implementation_version = '%s.%s.%s' % (sys.pypy_version_info.major,
                                               sys.pypy_version_info.minor,
                                               sys.pypy_version_info.micro)
        if sys.pypy_version_info.releaselevel != 'final':
            implementation_version = ''.join([
                implementation_version, sys.pypy_version_info.releaselevel
            ])
    elif implementation == 'Jython':
        implementation_version = platform.python_version()  # Complete Guess
    elif implementation == 'IronPython':
        implementation_version = platform.python_version()  # Complete Guess
    else:
        implementation_version = 'Unknown'

    return {'name': implementation, 'version': implementation_version}  # {'name': 'CPython', 'version': '3.6.5'}


def info():
    """Generate information for a bug report."""
    try:
        platform_info = {
            'system': platform.system(),        # Returns the system/OS name
            'release': platform.release(),      # Returns the system's release
        }
    except IOError:
        platform_info = {
            'system': 'Unknown',
            'release': 'Unknown',
        }

    implementation_info = _implementation()
    urllib3_info = {'version': urllib3.__version__}
    chardet_info = {'version': chardet.__version__}

    pyopenssl_info = {
        'version': None,
        'openssl_version': '',
    }
    if OpenSSL:
        pyopenssl_info = {
            'version': OpenSSL.__version__,
            'openssl_version': '%x' % OpenSSL.SSL.OPENSSL_VERSION_NUMBER,
        }
    cryptography_info = {
        'version': getattr(cryptography, '__version__', ''),
    }
    idna_info = {
        'version': getattr(idna, '__version__', ''),
    }

    # OPENSSL_VERSION_NUMBER doesn't exist in the Python 2.6 ssl module.
    system_ssl = getattr(ssl, 'OPENSSL_VERSION_NUMBER', None)
    system_ssl_info = {
        'version': '%x' % system_ssl if system_ssl is not None else ''
    }

    return {
        'platform': platform_info,
        'implementation': implementation_info,
        'system_ssl': system_ssl_info,
        'using_pyopenssl': pyopenssl is not None,
        'pyOpenSSL': pyopenssl_info,
        'urllib3': urllib3_info,
        'chardet': chardet_info,
        'cryptography': cryptography_info,
        'idna': idna_info,
        'requests': {
            'version': requests_version.__version__,
        },
    }


def main():
    """Pretty-print the bug information as JSON."""
    print(json.dumps(info(), sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
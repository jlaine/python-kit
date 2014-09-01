"""
Prismic.io python library.
"""

__title__ = 'prismic'
__version__ = '0.1.1'
__author__ = 'Prismic Team'
__license__ = 'Apache 2'

from .api import get, Api, SearchForm, Document
from .fragments import Fragment

# Set a default logger to prevent "No handler found" warnings
import logging
try:  # Python >=2.7
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

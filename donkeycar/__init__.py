__version__ = '4.1.0-dev'

print('using donkey v{} ...'.format(__version__))

import sys

if sys.version_info.major < 3:
    msg = 'Donkey Requires Python 3.6 or greater. You are using {}'.format(sys.version)
    raise ValueError(msg)

# The default recursion limits in CPython are too small.
sys.setrecursionlimit(10**5)

from .vehicle import Vehicle
from .memory import Memory
from . import utils
from . import config
from . import contrib
from .config import load_config

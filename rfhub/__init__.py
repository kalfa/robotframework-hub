import pkg_resources
from .version import __version__

import rfhub.kwdb

# this will be defined once the app starts
KWDB = None

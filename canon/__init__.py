from . import constants
from . import parsers
from . import printers
from . import sessions
from . import utils

from .printers import MG5700

from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests

# Disable requests's InsecureRequestWarning's
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

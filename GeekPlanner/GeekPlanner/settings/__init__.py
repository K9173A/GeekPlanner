"""
Chooses which settings should be imported depending on existence of
GEEKPLANNER_DEVELOPMENT environment variable.
"""
from .base import *


if os.environ.get('GEEKPLANNER_DEVELOPMENT', None) is None:
    from .production import *
else:
    from .development import *

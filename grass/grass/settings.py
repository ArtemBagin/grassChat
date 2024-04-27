from pathlib import Path
import os
import environ
from .base import *

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env()

if env.get_value('SETTINGS') == 'dev':
    from .dev import *
elif env.get_value('SETTINGS') == 'prod':
    from .prod import *



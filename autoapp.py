"""Create an application instance."""
from flask.helpers import get_debug_flag

from daily_pulse.app import create_app
from daily_pulse.config import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
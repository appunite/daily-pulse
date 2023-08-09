import asyncio
import functions_framework

from daily_pulse.handler.common import handler
from daily_pulse.config import config

@functions_framework.http
def daily_pulse(request) -> str:
    if not request.headers.get('Authorization') == f"Bearer {config['AUTH_CODE']}":
        return 'Authorization header invalid', 403

    return asyncio.run(handler(request))

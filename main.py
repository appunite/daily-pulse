import asyncio
import functions_framework

from daily_pulse.handler.common import handler
from daily_pulse.config import config


@functions_framework.http
def daily_pulse(request) -> str:
    if not request.headers.get("x-dailypulse-authorization") == f"Bearer {config['AUTH_CODE']}":
        return "Authorization header invalid", 403

    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": config["ORIGIN_DOMAIN"],
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Authorization",
            "Access-Control-Max-Age": "3600",
            "Access-Control-Allow-Credentials": "true",
        }
        return ("", 204, headers)

    headers = {
        "Access-Control-Allow-Origin": config["ORIGIN_DOMAIN"],
        "Access-Control-Allow-Credentials": "true",
    }

    return asyncio.run(handler(request))

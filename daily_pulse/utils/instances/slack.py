import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from daily_pulse.config import config

slack_token = config["SLACK_BOT_TOKEN"]
slack_client = WebClient(token=slack_token)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = None
slack_client = None

def initBitLy(app):
    global slack_token, slack_client

    slack_token = app.config.get("SLACK_BOT_TOKEN")
    slack_client = WebClient(token=slack_token)

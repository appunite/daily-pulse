"""Application configuration."""
import os
from datetime import timedelta


class Config(object):
    """Base configuration."""

    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
    DEBUG_MODE = os.environ.get('DEBUG_MODE', 'FALSE')
    LLM_TEMP = os.environ.get('LLM_TEMP', 'FALSE')
    LLM_CREATIVE_TEMP = os.environ.get('LLM_CREATIVE_TEMP', 'FALSE')


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    SLACK_BOT_CHANNEL = os.environ.get('SLACK_BOT_CHANNEL')
    BITLY_TOKEN = os.environ.get('BITLY_TOKEN')


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    SLACK_BOT_CHANNEL = os.environ.get('SLACK_BOT_CHANNEL', 'C057MGHDX7B')
    BITLY_TOKEN = os.environ.get('BITLY_TOKEN', '')

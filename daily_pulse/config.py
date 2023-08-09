"""Application configuration."""
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY"),
    "SLACK_BOT_TOKEN": os.environ.get("SLACK_BOT_TOKEN"),
    "SLACK_BOT_CHANNEL": os.environ.get("SLACK_BOT_CHANNEL"),
    "BITLY_TOKEN": os.environ.get("BITLY_TOKEN"),
    "DEBUG_MODE": os.environ.get("DEBUG_MODE", "FALSE"),
    "LLM_TEMP": os.environ.get("LLM_TEMP", 0),
    "LLM_CREATIVE_TEMP": os.environ.get("LLM_CREATIVE_TEMP", 1),
    "GET_PAGE_CONTENT_HOOK": os.environ.get("GET_PAGE_CONTENT_HOOK"),
    "AUTH_CODE": os.environ.get("AUTH_CODE"),
}

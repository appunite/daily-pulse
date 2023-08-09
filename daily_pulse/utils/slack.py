from string import Template
from daily_pulse.config import config
from daily_pulse.utils.instances.slack import slack_client

def sendMessageToChannel (text="", blocks=None, previous_response=None):
  thread_ts = None if previous_response is None else previous_response['ts']

  return slack_client.chat_postMessage(
        channel=config['SLACK_BOT_CHANNEL'],
        text=text,
        blocks=blocks,
        type="mrkdwn",
        thread_ts=thread_ts
  )

def getSlackMessageAsPlainText (title, cta, documents_summarized_combined):
  message_template = Template('*$title*\n\n$documents_summarized_combined\n\n$cta')
  return message_template.safe_substitute(title=title, documents_summarized_combined=documents_summarized_combined, cta=cta)
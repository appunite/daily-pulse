"""Notion data to shortened text handler"""
from daily_pulse.utils.page import getPageWithDocument
from daily_pulse.utils.slack import sendMessageToChannel
from daily_pulse.utils.summarize import getSummarizedAllDayMessage

async def bootstrap (raw_pages):
    pages = [getPageWithDocument(raw_page) for raw_page in raw_pages] 
    no_pages = len(pages) == 0
    if no_pages:
        return
    
    today_message_text = await getSummarizedAllDayMessage(pages)
    sendMessageToChannel(text=today_message_text)

def hasSupportedContentType(request):
    content_type = request.headers.get('Content-Type')
    return content_type == 'application/json'

async def handler(request):
    if (hasSupportedContentType(request)):
        raw_pages = request.json["pages"]
        await bootstrap(raw_pages)
        return 'OK', 200
    else:
        return 'Content-Type not supported', 415

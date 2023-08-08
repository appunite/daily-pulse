import requests
from daily_pulse.utils.instances.bitly import bitly_token

BITLY_SHORTEN_URI = 'https://api-ssl.bitly.com/v4/bitlinks'

def getBitlyShortenReqContent (title, url):
  return {
    "long_url": url,
    "domain": "bit.ly",
    "group_guid": "BmapbB5WwpG",
    "title": title,
    "tags": [
      "prasowka",
      "adr"
    ]
  }

def getBitlyShortenReqHeaders ():
  return {
      "Authorization": f"""Bearer {bitly_token}""",
      "Content-Type": "application/json"
  }

def getShortenedUrl (title, url):
  json = getBitlyShortenReqContent(title, url)
  headers = getBitlyShortenReqHeaders()
  resp = requests.post(BITLY_SHORTEN_URI, json=json, headers=headers)
  respJson = resp.json()

  return respJson['link']
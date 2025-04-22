import requests
import json

#content_id_list should be a list of the content ids to purge
#language is optional...default is English but can be changed (eg. "smxx" for all)
def content_purge(url, token, cookie, content_id_list, language="en"):

  url +=  "rs/content/purge"

  payload = json.dumps({
    "languageCode": language,
    "contentIds": content_id_list
  })

  headers = {
    'Content-Type': 'application/json',
    'Authorization': token,
    'Cookie': 'JSESSIONID=' + cookie
  }

  response = requests.request("POST", url, headers=headers, data=payload)

def media_category_purge(url, token, cookie, content_id_list, language="en"):

  url +=  "rs/hierarchy/purge"

  payload = json.dumps({
    "languageCode": language,
    "contentIds": content_id_list
  })

  headers = {
    'Content-Type': 'application/json',
    'Authorization': token,
    'Cookie': 'JSESSIONID=' + cookie
  }

  response = requests.request("POST", url, headers=headers, data=payload)
#this module contains endpoints that aren't documented but are still useful
import requests
import json

#section_id_list and channel_id are required
#section_id_list should be a list of the section ids to publish
#channel_id should be a single integer value (eg. 1)
#branch is optional (default is False) but can be changed to branch=True
#language is also optional (default is English)
def section_publish(url, token, cookie, section_id_list, channel_id, branch=False, language="en"):

  url +=  "rs/task/repository"

  payload = json.dumps({
    "taskType":"channelPublish",
    "channel":channel_id,
    "sections":section_id_list,
    "branch":branch,
    "publishCompleteChannel":False,
    "publishOptions":{"publishArchiveSections":True},
    "taskLevel":"section",
    "selectedLanguage":language
  })

  headers = {
    'Content-Type': 'application/json',
    'Authorization': token,
    'Cookie': 'JSESSIONID=' + cookie
  }

  response = requests.request("POST", url, headers=headers, data=payload)
#this module contains media endpoints 
import requests
import json

#media_id is required and should be a single integer value (eg. 1)
#language is optional (default is smxx) but can be changed (eg. language="en")
def get_media(url, token, cookie, media_id, language="smxx"):

  url +=  "rs/media/" + str(media_id) + "/" + language

  payload = json.dumps({})

  headers = {
    'Content-Type': 'application/json',
    'Authorization': token,
    'Cookie': 'JSESSIONID=' + cookie
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  output = response.json()
  return output
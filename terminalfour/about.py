import requests
import json

def about_environment(url, token, cookie):

  url +=  "rs/about/environment"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Authorization': token,
    'Cookie': 'JSESSIONID=' + cookie
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)

def about_database(url, token, cookie):

  url += 'rs/about/database'

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Authorization': token,
    'Cookie': 'JSESSIONID=' + cookie
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)
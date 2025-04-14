#authorize
import requests
import base64

class Terminalfour:
	def __init__(self, url, user, password):
		self.url = url
		self.user = user
		self.password = password
		self.jsession_id = ''
		self.access_token = ''
	
	def connect(self):
		connect_url = self.url
		user_pass = f"{self.user}:{self.password}"
		b64_user_password = base64.b64encode(user_pass.encode()).decode()
		auth_string = 'Basic ' + b64_user_password
		connect_url = self.url + "rs/authorize-implicit?client_id=site_manager_client&response_type=token"

		connect_payload = {}
		connect_headers = {
		  'Accept': 'application/json',
		  'Authorization': auth_string
		}

		first_response = requests.request("GET", connect_url, headers=connect_headers, data=connect_payload)

		initial_auth_token = first_response.json()['authenticityToken']
		self.jsession_id += first_response.cookies.get("JSESSIONID")

		auth_url = self.url + "rs/authorize-implicit/decision?client_id=site_manager_client&oauthDecision=allow&session_authenticity_token=" + initial_auth_token

		auth_payload = {}
		auth_headers = {
		  'Accept': 'application/json',
		  'Cookie': 'JSESSIONID=' + self.jsession_id
		}

		second_response = requests.request("GET", auth_url, headers=auth_headers, data=auth_payload)
		self.access_token += second_response.json()['accessToken']
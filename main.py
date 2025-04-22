#main.py
import terminalfour
import json

t4_url = 'http://localhost:8080/terminalfour/'
t4_user = 'brian'
t4_password = '<insert password>'
content_ids = [184,185]
#section_id_list = [268]
#channel_id = 1
#media_id = 121

t4 = terminalfour.Terminalfour(t4_url, t4_user, t4_password)
try:
	t4.connect()
	print("Successfully connected to Terminalfour.")
	#print("accessToken: " + t4.access_token)
	#print("JSESSIONID: " + t4.jsession_id)
except:
	print("Error connecting to Terminalfour.")

#begin main script here	
try:
	#print("Env Info: ")
	#terminalfour.about_environment(t4_url, t4.access_token, t4.jsession_id)
	#purge content_ids
	terminalfour.content_purge(t4_url, t4.access_token, t4.jsession_id, content_ids)
	#purge media category
	#terminalfour.media_category_purge(t4_url, t4.access_token, t4.jsession_id, content_ids)
	#section publish
	#terminalfour.section_publish(t4_url, t4.access_token, t4.jsession_id, section_id_list, channel_id)
	#get a media id
	#results = json.dumps(terminalfour.get_media(t4_url, t4.access_token, t4.jsession_id, media_id))
except Exception as e:
	print(e)
#print(results)
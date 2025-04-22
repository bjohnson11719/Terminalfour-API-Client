#media report.py
import terminalfour
import json
import csv

t4_url = 'http://localhost:8080/terminalfour/'
t4_user = 'brian'
t4_password = '<insert password>'

t4 = terminalfour.Terminalfour(t4_url, t4_user, t4_password)
try:
	t4.connect()
	print("Successfully connected to Terminalfour.")
except:
	print("Error connecting to Terminalfour.")

#begin main script here	
ids = [
10,
11,
13,
16,
19,
20,
35,
40,
41,
42,
43,
45,
46,
47,
67,
12,
73,
102,
121,
122,
136,
133,
139
]

header_row = ["ID", "Version Number", "Name", "Last Modified Date", "Last Modified By",\
	"File Type", "File Path", "File Name", "Size (Bytes)", "Description / Alt Text"]

results = []

try:
	for id in ids:
		output_json = terminalfour.get_media(t4_url, t4.access_token, t4.jsession_id, id)
		results.append([output_json['id'],output_json['version'],output_json['name'],\
			output_json['elements']['Media#4:4']['lastModified'],output_json['lastModifiedBy'],\
			output_json['typeName'],output_json['mediaPath'],output_json['fileName'],\
			output_json['mediaSize'],output_json['description']])
except Exception as e:
	print(e)

output_file = "test_file.csv"

with open(output_file, 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(header_row)
	csvwriter.writerows(results)
csvfile.close()
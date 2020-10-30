#!/bin/env python 


#Import requests and JSON 

import requests
import json

url = "https://launchlibrary.net/1.3/agency"
response = requests.get(url)

#Define a variable that can format response in a more clear manner

def jsonprint(object):
	text = json.dumps(object, indent=4)
	print(text)

#The next 2 lines are tests to see if def jsonprint works
#dict = jsonprint(response.json())
#print(dict)

#Verify whether the agency for is a launch service provider

agencies = response.json()['agencies']
jsonprint(agencies)

for d in agencies:
	print(d["name"])
	if d["islsp"] == 0:
		print('is not a Launch Service Provider')
		print("\n")
	elif d["islsp"] == 1:
		print('is a Launch Serive Provider')
		print("\n")



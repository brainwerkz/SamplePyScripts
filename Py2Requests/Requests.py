#!/usr/bin/python3

import requests

r = requests.get('http://136.62.71.28/')

#print (r.status_code)

print (r.url)

if (r.status_code) == 200:
	print("The website is up!!")
else:
	print("Sorry, the website is down now")
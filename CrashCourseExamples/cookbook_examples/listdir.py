#!/usr/local/bin/python3

import os
dir = raw_input('What directory would you like to search? Plese enter the full directory path.')
files = os.listdir(dir)

for name in files:
	try:
		print(name)
	except UnicodeEncodeError:
		print(bad_filename(name))


#print(files)

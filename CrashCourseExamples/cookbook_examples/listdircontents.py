#!/usr/local/bin/python3

import os
import os.path
import glob


pyfiles = glob.glob('*.py')

#Get file sizes, etc.
#name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
#				for name in pyfiles]
#for name, size, mtime in name_sz_date:
#	print(name, size, mtime)

#Alternative to above
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
	print(name, meta.st_size, meta.st_mtime)


	
#excluded just for the above script	
#dir = input('What directory would you like to search? Plese enter the full directory path.')
#files = os.listdir(dir)

#for name in files:
#	try:
#		print(name)
#	except UnicodeEncodeError:
#		print(bad_filename(name))


#print(files)

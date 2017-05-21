import getpass
# name = getpass.getuser()
# print(name)




# this one also works to get username
import os
import requests

newname = (os.getlogin())
# print (os.getlogin())

print('Hello', newname)

me = (os.getcwd())

new = (os.getuid())

another = (os.getgroups())




print(me)
print(new)
print(another)
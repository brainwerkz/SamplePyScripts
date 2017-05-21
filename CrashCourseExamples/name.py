#!/usr/local/bin/python3

name = "linda lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#combine first and last
first_name = "linda   "
#first_name.lstrip()
#first_name.rstrip()
last_name = "lovelace"
full_name = first_name.strip() + " " + last_name
message = "Hello, " + full_name.title() + "! \n\tI'd love a blowjob from you!!!"
print (message)

#famous quote
famous_quote = 'Albert Einstein once said,' '\n\t"A person who never made a mistake never tried anything new."'
print(famous_quote)

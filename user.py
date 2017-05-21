#!/usr/bin/python

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
    
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
   

for key, value in user_0.items():
    print('username')
    #print(value)
    
#Names and programming languages

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }

print("\n")
for name, language in favorite_languages.items():
#for name in favorite_languages:
    print(name.title() + "'s favorite language is " +
        language.title() + ".")


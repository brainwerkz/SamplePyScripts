#!/usr/bin/python

#Names and programming languages

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }
    
#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
#    print(name.title())
    
#    if name in friends:
#        print(" Hi " + name.title() +
#            ", I see your favorite language is " +
#            favorite_languages[name].title() + "!")
            
#    if 'erin' not in favorite_languages.keys():
#        print("Erin, please take our poll!")
                
#    if 'sarah' in favorite_languages.keys():
#        print('Sarah, I would love to make love to you!')
                
for name in sorted (favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll!")

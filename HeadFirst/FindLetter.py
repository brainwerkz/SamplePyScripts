#!/usr/bin/python3

vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search in for vowels: ")
found = []
for letter in str.lower(word):
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print (vowel)

print(found)
print(word)
print(len(word))
print(len(found))


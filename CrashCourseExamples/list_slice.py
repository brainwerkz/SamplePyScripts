#!/usr/local/bin/python3

players = ['brittney','alicia','dianna','laura','milla']
print(players[0:3])

print(players[1:4])

print(players[2:4])

print(players[-1])

print(players[:5])

print(players[1:])

print('Here are the top 3 actresses:')
for player in players[:3]:
	print(player.title())

my_foods = ['pizza','hamburger','tacos','steak']
friend_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print("\nMyfriend's favorite foods are:")
print(friend_foods)

print('\nMy favorite foods are:')
print(my_foods)

my_foods.append('chinese')
friend_foods.append('salad')

print('My favorite foods are:')
print(my_foods)

print("\nMyfriend's favorite foods are:")
print(friend_foods)

print('Here are my favorite foods:')
for myfav in my_foods[:]:
	print(myfav.title())
	
print("\nHere are my friend's favorite foods:")
for friendfav in friend_foods[:]:
	print(friendfav.title())

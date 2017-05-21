#!/usr/bin/python

alien_0 = {}

print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0['sex'] = 'female'

print("The sex of the alien is " + alien_0['sex'] + "!")
#print(alien_0)

alien_0['sex'] = 'hermaphrodite'

print("The sex of the alien is now " + alien_0['sex'] + "!")


alien_0 = {'sex': 'female', 'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("\noriginal x-position: " + str(alien_0['x_position']))
#move the alient to the right.
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3
    
#the new position is te old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

print(alien_0)
del alien_0['sex']
print(alien_0)


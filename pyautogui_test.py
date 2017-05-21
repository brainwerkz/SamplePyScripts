#!/usr/bin/python3

import pyautogui
pyautogui.alert('This is an alert box.')

pyautogui.confirm('Shall I proceed?') 

pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C']) 

pyautogui.prompt('What is your name?') 

pyautogui.password('Enter password (text will be hidden)') 


im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')
im2 = pyautogui.screenshot('my_screenshot2.png')




# this is a test section You can also locate where an image is on the screen:


button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
button7location (1416, 562, 50, 41)
buttonx, buttony = pyautogui.center(button7location)
buttonx, buttony (1441, 582)
pyautogui.click(buttonx, buttony) # clicks the center of where the button was found

# The locateCenterOnScreen() function returns the center of this match region:

buttonx, buttony = pyautogui.locateCenterOnScreen('button.png') # returns (x, y) of matching region
buttonx, buttony (1441, 582)
pyautogui.click(buttonx, buttony) # clicks the center of where the button was found

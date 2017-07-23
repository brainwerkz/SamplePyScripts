#!/usr/local/bin/python3

import webbrowser
import time
#webbrowser.open('http://www.python.org')

c = webbrowser.get('firefox')
c.open('http://www.python.org')
time.sleep(3) # delays for X seconds
c.open_new_tab('http://www.brainwerkz.com')

import os
from webbot import Browser
from time import sleep

web = Browser()
print('idk what to put here lol')
print('if you this this just fill the form')
print('================================')
print('G = www.Google.com')
print('Use Your own URL')
print('Leave Blank For Default Website')
print('================================')
website = input('Website: ')

if website == 'G':
    web.go_to('https://www.google.com/')

if website == '':
    web.go_to('https://pypi.org/project/webbot')

else:
    web.go_to(website)

while True:
    sleep(0.1)

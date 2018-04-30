#! /usr/bin/python3

import requests, sys, bs4

#if command line argument get web address from argument
if len(sys.argv) > 1:
    address = sys.argv[1]
#if no command line argument then pasted from clipboard
else:
    address = pyperclip.paste()

site = requests.get(address)

try:
    site.raise_for_status()
except Exception as e:
    print("didn't work, there was a problem: {}".format(e))

siteSoup = bs4.BeautifulSoup(site.text)





         

# python3 -m pip install beautifulsoup4
# python3 -m pip install requests

# pip3 install html5lib

import os
import requests
from bs4 import BeautifulSoup

url = input("Enter a website to extract the URL's from: ")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data, "html5lib")

print ('Started.')

for link in soup.find_all('a'):
    print (link.get('href').strip())
    print ('\t')
    print ((link.text).strip())

# for link in soup.find_all('p'):
#    print(link.get('p'))

# Get the page title from the head section
#for title in soup.find_all('title'):
head_tag = soup.head
title_tag = head_tag.contents[0]
print ((title_tag.contents))

print ('Finished.')

# python3 -m pip install beautifulsoup4
# python3 -m pip install requests

import os
import requests
from bs4 import BeautifulSoup

url = input("Enter a website to extract the URL's from: ")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data, "html5lib")

print ('Started.')

for link in soup.find_all('a'):
    print (link.get('href'))
    print (link.text)

# for link in soup.find_all('p'):
#    print(link.get('p'))

print ('Finished.')

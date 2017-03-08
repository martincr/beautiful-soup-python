# basic web scraper

# See https://beautiful-soup-4.readthedocs.io/en/latest/
# See https://docs.python.org/3.0/library/urllib.request.html

from bs4 import BeautifulSoup
import urllib

r = urllib.request.urlopen(
    'https://web.archive.org/web/20111010022320/http://maxkle.in/how-to-make-your-startup-grow/').read()
soup = BeautifulSoup(r, 'html5lib')

# soup.prettify()

# print (soup.find_all('p'))

#soup.find_all(class_="entry")

#print (soup.select("entry"))

# Prints all the paragraphs
#print (soup.find_all("p"))

#soup.select_one(".entry")

#print(soup.prettify())

#print (soup.find_all("p"))

#for paragraph in soup.find_all('.entry'):
#    print(paragraph.get('p'))

# Extracting all the text from a page
#print(soup.get_text())

# print (soup.find_all("h2"))

# Print the paragraphs only in a specific div tag
body_text = soup.find(class_="entry")

paragraph_text = body_text.find_all("p")

print(paragraph_text)

#for link in soup.find_all(class_="entry"):
#    print(link.get_text())

#body_text = soup.find(class_="entry")

#print (body_text)
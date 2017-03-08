import requests
from bs4 import BeautifulSoup


# Create a variable with the url
url = 'https://web.archive.org/web/20111010022320/http://maxkle.in/how-to-make-your-startup-grow/'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'html5lib')

# View the tbody tag of the soup object
table = soup.find('p')

# Print all the links on a page to the Terminal
for link in soup.find_all('a'):
    print(link.get('href'))

# Print all the paragraphs on a page to the Terminal
for link in soup.find_all('p'):
    print(link.get('p'))
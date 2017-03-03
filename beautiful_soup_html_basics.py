import requests
from bs4 import BeautifulSoup


# Create a variable with the url
url = 'http://connectedhomes.net'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'html5lib')

# View the title tag of the soup object
for t in soup.find_all('p'):
    print (t.get_text() + '\n')
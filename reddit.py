from bs4 import BeautifulSoup
import urllib

redditFile = urllib.request.urlopen("http://www.reddit.com")
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml, 'html5lib')
redditAll = soup.find_all("a")

for links in soup.find_all('a'):
    print (links.get('href'))
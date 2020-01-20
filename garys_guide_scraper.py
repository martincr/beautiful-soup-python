import requests

from bs4 import BeautifulSoup

# Open a browser-version of the newsletter using requests:
r = requests.get("https://www.garysguide.com/events/newsletter/2b9694ceb0584ca689f942654ad3f85a/42j9w5")

# Find RECENTLY READ section:
# TO DO
inner_text = soup.find("<font style="background-color:#ffff99; padding:2px;">RECENTLY READ</font>", id="price").text.strip()


# Finish after two <br> tags
# TO DOp

# Get all the links
soup = BeautifulSoup(r.text, "html5lib")
for links in soup.find_all("a"):
    print (links)

# with open("garys_guide.txt") as fp:
#     soup = BeautifulSoup(fp, "html5lib")

# soup = BeautifulSoup("<html>data</html>", "html5lib")
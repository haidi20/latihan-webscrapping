import requests
from bs4 import BeautifulSoup

# from urllib2 import urlopen
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# URL = 'https://10.151.6.250:8443'
# soup = BeautifulSoup(urlopen(URL))

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
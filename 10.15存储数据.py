from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bsObj = BeautifulSoup(html, 'lxml')
image = bsObj.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve(image, 'logo.jpg')

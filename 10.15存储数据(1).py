from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.jnugeek.cn')
bsObj = BeautifulSoup(html, 'lxml')
image = bsObj.find('a', {'class': 'navbar-brand', 'href': '#the top'}).find('img')['src']
image = 'http://www.jnugeek.cn' + image
# urlretrieve根据文件的url下载文件
urlretrieve(image, 'logo.png')

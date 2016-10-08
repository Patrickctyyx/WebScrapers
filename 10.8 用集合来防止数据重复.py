from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# set是集合，没有重复的元素，元素无先后顺序
pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')

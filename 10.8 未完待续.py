from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# urlparse用法示例
# >>> from urllib.parse import urlparse
# >>> o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
# >>> o
# ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
#             params='', query='', fragment='')


def getInternalLinks(bsObj, includeUrl):
    # includeUrl是主界面的url
    includeUrl = urlparse(includeUrl).scheme + '://' + urlparse(includeUrl).netloc
    internalLinks = []
    # | 匹配以竖线 (|) 字符分隔的任何一个元素
    # 这里是匹配/或者包含当前url的链接
    for link in bsObj.findAll('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startswitch('/'):
                    internalLinks.append(includeUrl + link.attrs['href'])
    return internalLinks


def getRxternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for 

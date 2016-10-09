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
                # 如果是包含原链接的，就不用了？？？
                if link.attrs['href'].startswitch('/'):
                    internalLinks.append(includeUrl + link.attrs['href'])
    return internalLinks


def getRxternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 以http/www开头，而且不包含原链接
    for link in bsObj.findAll('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, 'lxml')
    externalLinks = getRxternalLinks(bsObj, urlparse(startingPage).netloc)
    # 递归，直到找到外部链接，可能是从其他内部链接中找到的
    # 其中外部链接是找到得中的任意一个
    if len(externalLinks) == 0:
        print('No external links, looking from the internal ones.')
        domain = urlparse(startingPage).scheme + '://' + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLinks(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingsite):
    externalLink = getRandomExternalLinks(startingsite)
    print('Random external site:' + externalLink)
    followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')

# 里面还是有问题而且效率依旧很低，先放在这里

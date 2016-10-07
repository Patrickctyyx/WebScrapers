from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# 设置seed可以让同样的seed生成的随机数相同
random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
links = getLinks('/wiki/Kevin_Bacon')
for i in range(5):
    # randint是生成括号里面范围数字的任意一个数字，闭区间
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

# 爬取一个人随机的一个相关的人，一共五次

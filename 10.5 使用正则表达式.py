from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.jnugeek.cn/static/home.html')
bsObj = BeautifulSoup(html, 'lxml')
for image in bsObj.findAll('img'):
    print(image)

html2 = urlopen('https://en.wikipedia.org/wiki/Stephen_Curry')
bsObj2 = BeautifulSoup(html2, 'lxml')
# ^是用来匹配开头的字符
# ?可以匹配0个到1个
# ?!表示不匹配后面跟的表达式
# .用来匹配除换行符外任意的1个
# *可以匹配0个到无限个
# 这里匹配的是/wiki/开头，不存在:的
for link in bsObj2.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

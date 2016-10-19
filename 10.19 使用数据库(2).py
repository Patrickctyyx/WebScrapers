from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='passwd',
                       db='mysql',
                       # 进去的数据当做utf-8
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
# execute里面直接就是数据库语句了
cur.execute('USE patscraper')

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")', (title, content))
    # 如果是插入删除修改数据不要忘记提交
    cur.connection.commit()


def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    title = bsObj.find('h1').get_text()
    content = bsObj.find('div', {'id': 'mw-content-text'}).find('p').get_text()
    store(title, content)
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Durant')
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    # 不要忘记关掉这两项，顺序不要反
    cur.close()
    conn.close()


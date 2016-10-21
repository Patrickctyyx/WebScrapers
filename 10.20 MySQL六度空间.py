from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='passwd',
                       db='mysql',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
cur.execute('USE patscraper')


# 只有不重复才装载到数据库
def insertPageIfNotExists(url):
    # 注意这里execute里面的语法
    cur.execute('SELECT * FROM pages_2 WHERE url = %s', url)
    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages_2 (url) VALUES (%s)', url)
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()['id']


def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM links WHERE from_page_id = %s AND to_page_id = %s',
                (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (from_page_id, to_page_id) VALUES (%s, %s)',
                    (int(fromPageId), int(toPageId)))
        conn.commit()


pages = set()


def getLinks(pageUrl, recursionLevel):
    global pages
    # 递归最多到第五层
    if recursionLevel > 4:
        return ''
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage, recursionLevel + 1)


getLinks('/wiki/Kevin_Durant', 0)
cur.close()
conn.close()

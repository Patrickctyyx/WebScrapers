from urllib.request import urlopen
from urllib.request import unquote
from bs4 import BeautifulSoup
import unittest
import re
import random


class TestWikipedia(unittest.TestCase):

    bsObj = None
    url = None

    def test_pageProperties(self):
        global bsObj
        global url

        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url), 'lxml')
            titles = self.titleMatchesURL()
            self.assertEqual(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print('Done!')

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find('h1').get_text()
        # index是用来定位，具体是括号里面的东西在第几位
        # 这里是为了得到url中的Monty_Python
        urlTitle = url[(url.index('/wiki/') + 6):]
        urlTitle = urlTitle.replace('_', ' ')
        # 解码
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find('div', {'id': 'mw-content-text'})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        global bsObj
        links = bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        link = 'http://en.wikipedia.org' + newArticle
        return link

# 总觉得这样测试有点傻
# 不过这里我也不知道想测试什么...
# 不过爬虫+单元测试似乎是个不错的组合
if __name__ == '__main__':
    unittest.main()

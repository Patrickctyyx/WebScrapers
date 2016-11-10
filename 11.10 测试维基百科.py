from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest


class TestWikipedia(unittest.TestCase):

    bsObj = None

    # setUpClass代替setUp，使得只用加载一次
    # 可以一次测试所有内容
    def setUpClass():
        global bsObj
        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        bsObj = BeautifulSoup(urlopen(url), 'lxml')

    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find('h1').get_text()
        self.assertEqual('Monty Python', pageTitle)

    def test_content(self):
        global bsObj
        content = bsObj.find('div', {'id': 'mw-content-text'})
        self.assertIsNotNone(content)


if __name__ == '__main__':
    unittest.main()

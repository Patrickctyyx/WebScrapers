from scrapy.selector import Selector
from scrapy import Spider
from PatrickScrape.items import Article


class ArticleSpider(Spider):
    # 指定了爬虫的名字
    # 用$scrapy crawl article来进行该爬虫
    name = 'article'
    # 可选，允许爬取的列表
    allowed_domains = ['en.wikipedia.org']
    # 要爬取的列表
    start_urls = ['http://en.wikipedia.org/wiki/Main_Page',
                  'http://en.wikipedia.org/wiki/Python_%28programming_language%29']

    # 参数的response来自于解析上面URL函数得到的Response对象
　　　　def parse(self, response):
        # 用来储存得到的信息，相当于数据库储存对象
        item = Article()
　　　　　　　　# 提取response中的h1
　　　　　　　　# xpath还要再看看
        title = response.xpath('//h1/text()')[0].extract()
        print('Title is:' + title)
        item['title'] = title
        return item

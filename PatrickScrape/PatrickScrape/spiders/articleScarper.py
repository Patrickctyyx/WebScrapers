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
        # xpath是很强的模块
        # 这里//h1是获得所有的h1
        # /text()是获得其中的文本内容(过滤掉html标签)
        # [0]是因为结果是一个list，以此来取出其中元素
        # .extract()是用来过滤日志信息，获得消息本体
        # 整个下来title就是页面的标题了
        title = response.xpath('//h1/text()')[0].extract()
        print('Title is:' + title)
        # 然后把获得的信息储存在类似于数据库的item中
        item['title'] = title
        return item

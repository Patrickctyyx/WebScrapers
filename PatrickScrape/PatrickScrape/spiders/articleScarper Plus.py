from scrapy.spiders import CrawlSpider, Rule
from PatrickScrape.items import Article
from scrapy.linkextractors import LinkExtractor


class ArticleSpiderPlus(CrawlSpider):
    """和Spider不同的是，Crawlspider里面可以定义规则"""
    name = 'articles'
    allowed_damains = ['en_wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Main_Page',
                  'http://en.wikipedia.org/wiki/Python_%28programming_language%29']
    # 一个包含Rule对象的list
    # 每个Rule都定义了爬取对象的动作
    # SgmlLinkExtractor allow里面是正则
    # callback是用来调用string所指代的函数
    # follow指定了是否跟进response获得的链接
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'), ), callback='parse_item', follow=True)]

    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print('Title is:' + title)
        # 然后把获得的信息储存在类似于数据库的item中
        item['title'] = title
        return item

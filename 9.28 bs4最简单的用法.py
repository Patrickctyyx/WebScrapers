from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):

    # 可能出现的错误：
    # 该网址的信息收不到(httperror)
    # 或者bs对象没有所请求的属性，即原html无该标签(attr_error)

    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        # BeautifulSoup transfer the html content to a bsObject
        # which has attrs of html,such as head,body etc
        bsObj = BeautifulSoup(html.read(), 'xml')
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title

title = get_title('http://www.pythonscraping.com/pages/page1.html')
print(title)

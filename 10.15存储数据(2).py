import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

downloadDir = 'downloads'
baseUrl = 'http://www.jnugeek.cn'


# 获得绝对路径
def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = source
    elif source.startswith('www.'):
        url = 'http://' + source
    else:
        url = baseUrl + '/' +source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDir):
    # 得到相对路径
    path = absoluteUrl.replace(baseUrl, '')
    # 把要下载的文件放在指定目录中并且里面的内容和原网站上的一样
    path = downloadDir + path
    # 获得下载根目录名
    dire = os.path.dirname(path)

    # 如果不存在就创建目录
    if not os.path.exists(dire):
        os.makedirs(dire)

    return path


html = urlopen(baseUrl)
bsObj = BeautifulSoup(html, 'lxml')
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDir))

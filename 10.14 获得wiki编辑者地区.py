from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json


random.seed(datetime.datetime.now())


# 获得相关界面的url
def getLinks(articleUrl):
    html = urlopen(articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


# 通过wiki历史编辑记录界面提取出匿名编辑者ip
def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace('/wiki/', '')
    historyURL = 'http://en.wikipedia.org/w/index.php?title=' + pageUrl + '&action=history'
    print('history url:' + historyURL)
    html = urlopen(historyURL)
    bsObj = BeautifulSoup(html, 'lxml')
    ipAddresses = bsObj.findAll('a', {'class': 'mw-userlink mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


# 通过调用freegeoip的api来获得对应的国家地区城市
def getCountry(ipAddress):
    try:
        response = urlopen('http://freegeoip.net/json/' + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return [responseJson.get('country_name'), responseJson.get('region_name'), responseJson.get('city')]

# 爬取开始的界面
links = getLinks('http://en.wikipedia.org/wiki/Python_(programming_language)')

# 直到没有东西可爬取才借书
while len(links) > 0:
    for link in links:
        print('----------------')
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + ' is from ' + country[0] + ', ' + country[1] + ', ' + country[2])

    newLink = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newLink)

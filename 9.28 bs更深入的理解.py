from bs4 import BeautifulSoup
from urllib.request import urlopen
# html是一个httpResponse对象，如果要查看内容要使用read()方法
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html, 'lxml')
namelist = bsObj.findAll('span', {'class': 'green'})
for name in namelist:
    print(name.get_text())  # 标签的内容
    print(name)  # name是带标签的

html2 = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj2 = BeautifulSoup(html2, 'lxml')
# bs的find方法默认是遍历所有层次的内容的，这里的.children方法只得到第一层的结果
# 另外对应.chilren还有.descendants方法，遍历以下所有层
# 在不同层用find方法都可以，这里只是用.find()取代了.table
for siblings in bsObj2.find('table', {'id': 'giftList'}).children:
    print(siblings)
# .next_siblings方法用来找同一层中除了自己的元素
# 同样，还有.previous_siblings，.parents等等..
# 一个html文件就是一个树形的数据结构，而这些方法，就是对树元素的各种查找遍历之类的
for siblings in bsObj2.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(siblings)

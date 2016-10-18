import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.apple.com/mac/compare/results/?product1=macbook&product2=macbook-pro-retina-13')
bsObj = BeautifulSoup(html, 'lxml')
# findAll是把所有section参数收集并且以list的形式储存(遍历所有子标签)
# find其他和上面一样，但是只遍历下面一层标签
sections = bsObj.findAll('section')

csvFile = open('apple.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for section in sections:
        heads = section.findAll('h4')
        if not heads:
            continue
        titles = []
        for head in heads:
            # 不知道为什么这里必须吧数据储存在新的list里面，要不然改变不了heads
            titles.append(head.get_text())
        writer.writerow(titles)
        cls = section.findAll('p')
        columns = []
        i = 1
        for cl in cls:
            columns.append(cl.get_text())
            if i % 2 == 0:
                writer.writerow(columns)
                columns = []
            i += 1
finally:
    csvFile.close()

# 获取Mac比较界面Mac的参数的



import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.apple.com/mac/compare/results/?product1=macbook&product2=macbook-pro-retina-13')
bsObj = BeautifulSoup(html, 'lxml')
sections = []
content0 = bsObj.findAll('section')
sections.append(content0)
for content in bsObj.find('section').next_siblings:
    print(content)
    sections.append(content)

csvFile = open('apple.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    i = 0
    for section in sections:
        i += 1
        print(i)
        head = section.findAll('h4')
        print(head)
        writer.writerow(head.get_text())
        cls = section.finAll('p')
        print(cls)
        column = []
        for cl in cls:
            column.append(cl.get_text())
        writer.writerow(column)
finally:
    csvFile.close()

# 本来是想获取Mac比较界面Mac的参数的
# 然而有一些疑问
# BeautifulSoap的find，finaAll到底是用法是怎样
# 是返回第一个结果还是所有结果？


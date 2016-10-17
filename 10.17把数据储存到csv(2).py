import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html)
table = bsObj.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')

# 关于newline参数
# 如果为''，换行符就是原来的换行符
# 如果为None,换行符就都会变成\n
csvFile = open('editors.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['th', 'td']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()


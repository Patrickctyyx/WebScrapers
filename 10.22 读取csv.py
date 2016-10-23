from urllib.request import urlopen
from io import StringIO
import csv

# decode这里是因为直接读出来的csv文件包含大量换行符，不能成为StringIO对象
data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv')\
    .read().decode('ascii', 'ignore')
print(data)  # 是一行行的文本了
dataFile = StringIO(data)
print(dataFile)  # 是个对象
csvReader = csv.reader(dataFile)
print(csvReader)  # 是个对象，可迭代
# 把StringIO对象变成dict，key当然是第一行的字段名称
# 然后就把字段名那一行给省略掉啦
dictReader = csv.DictReader(dataFile)
# 要度出来就这样
print(dictReader.fieldnames)

for elem in dictReader:
    print(elem)

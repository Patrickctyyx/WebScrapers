from zipfile import ZipFile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO

wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
wordFile = BytesIO(wordFile)  # 把word读成二进制文件对象
document = ZipFile(wordFile)  # 解压(.docx文档都进行过压缩)
xml_content = document.read('word/document.xml')  # 括号里面是解压文件的名字
print(xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'lxml')
textStrings = wordObj.findAll('w:t')
for textElem in textStrings:
    print(textElem.text)  # 这里的.text和.get_text()没区别




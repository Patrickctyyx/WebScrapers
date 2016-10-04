from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'lxml')
images = bsObj.findAll('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
for img in images:
    print(img)

# using a 'lambda function' as an attr of findAll
# lambda的参数一定要是tag对象
results = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for rst in results:
    print(rst)

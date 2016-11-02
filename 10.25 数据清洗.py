from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string


def ngarms(input_content, n):
    # 用正则把换行符去掉，＋号是匹配0到多次
    input_content = re.sub('\n+', ' ', input_content)
    # 去掉形如[88]这种注释，*号是匹配1到多次
    input_content = re.sub('\[[0-9]\]*', '', input_content)
    # 把很多空格缩减成一个
    input_content = re.sub(' +', ' ', input_content)
    # 先用utf-8编码来消除转义字符
    input_content = bytes(input_content, 'UTF-8')
    # 忽略掉奇怪的acsii字符
    input_content = input_content.decode('ascii', 'ignore')
    input_content = input_content.split(' ')
    cleanInput = []
    for item in input_content:
        item = item.strip(string.punctuation)
        # 一个的字符都要过滤掉除了I A
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    output = []
    for i in range(len(cleanInput) - n + 1):
        output.append(cleanInput[i: i + n])
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'lxml')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngarm = ngarms(content, 2)
# OrderedDict是让dict有序
# sorted()第一个参数是一个可迭代对象,key是搜索的规则，比如这里是根据数组里面第二个元素排序，但是在这个的情景下有问题
# 当然刻可以自定义一个函数不一定要用匿名函数，当然返回值要能作为排序的条件
ngarm = OrderedDict(sorted(ngarm, key=lambda t: t[1], reverse=True))
print(ngarm)
print('3-grams count: ' + str(len(ngarm)))

from urllib.request import urlopen
import re
import string
import operator


def ngramOutput(input_content, n):
    # 用正则把换行符去掉，＋号是匹配0到多次
    input_content = re.sub('\n+', ' ', input_content).lower()
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
    output = {}
    # 统计每个词出现的频率
    for i in range(len(cleanInput) - n + 1):
        ngramTemp = ' '.join(cleanInput[i: i + n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(),
              'utf-8')
ngrams = ngramOutput(content, 2)
# operator.itemgetter相当于定义了一个函数
# 这个函数返回这个项目的第1个值，在这里是这样的，取决于参数
# 当然根据伤一次的key这里就是要跟一个函数来确定筛选的方法
sortedNgrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNgrams)

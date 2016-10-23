from urllib.request import urlopen
textPage = urlopen('https://www.ietf.org/rfc/rfc1149.txt')
print(textPage.read())

textPage2 = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
# 读取纯文本文件
# 得到的结果读出来就是不同的字符串
# 这时候就可以用str来转换编码方式了
print(str(textPage2.read(), 'utf-8'))

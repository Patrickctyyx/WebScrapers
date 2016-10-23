from urllib.request import urlopen
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import time
import smtplib

html = urlopen('http://item.jd.com/3212128.html')
bsObj = BeautifulSoup(html, 'lxml')
# 这里价格标签的内容是空的，应该是用JS动态渲染上去的
# 能力还达不到，先留一个坑
price = bsObj.findAll('strong', {'class': 'p-price'})
print(price)

# 初步想法是获取京东某个商品的价格
# 每隔一个小时重新获得这个价格
# 如果有改动就发邮件提醒
# 其实京东意境有降价提醒了...
# 然后这里涉及到的是动态界面的爬取，现在能力还达不到，只能后面再来了

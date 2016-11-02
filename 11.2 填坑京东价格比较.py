from selenium import webdriver
from selenium.webdriver.common.by import By  # 定位器
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 期望条件，触发状态
from email.mime.text import MIMEText
import time
import smtplib

# html = urlopen('http://item.jd.com/3212128.html')
# bsObj = BeautifulSoup(html, 'lxml')
# 这里价格标签的内容是空的，应该是用JS动态渲染上去的
# 能力还达不到，先留一个坑
# price = bsObj.findAll('strong', {'class': 'p-price'})
# print(price)

# 初步想法是获取京东某个商品的价格
# 每隔一个小时重新获得这个价格
# 如果有改动就发邮件提醒
# 其实京东意境有降价提醒了...
# 然后这里涉及到的是动态界面的爬取，现在能力还达不到，只能后面再来了

# 现在大体可以了哈哈哈
price = 9999999


def track_price(html):
    driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
    driver.get(html)
    global price
    while price >= 800:
        try:
            # WebDriverWait(driver, 10)这里指定了对象driver，最多等10s
            # 如果有后面的until里面的触发条件就提前触发
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'p-price'))
                # 这里两重括号不是重复，而是前面那个接受一个tuple为参数
                # 这个tuple相当于一个dict
                # 前面是key后面是value
            )
        finally:
            pre_price = price
            price = driver.find_element_by_class_name('p-price').text
            if price != pre_price:
                print(price)
            price = float(price[1:])
            if price < pre_price:
                sendMail('Price goes dowm!', 'Price is %d lower than last price' % (pre_price - price))
            else:
                time.sleep(3600)

    driver.close()

# 配置邮箱的服务器
mail_host = 'smtp.sina.com'
mail_user = 'chengtianyang523@sina.com'
mail_pswd = 'passwd'


def sendMail(subject, body):
    # 创建一个空邮件，下面就是放入内容
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'chengtianyang523@sina.com'
    msg['To'] = '873948000@qq.com'

    # 创建smtp实例，用smtp协议发邮件
    s = smtplib.SMTP()
    # 连接服务器，这里是新浪的
    s.connect(mail_host, 25)
    # 登陆账号，不然怎么发呢
    s.login(mail_user, mail_pswd)
    # 发邮件
    # 还有另外一种s.send_mail(sender, receiver)
    s.send_message(msg)
    # 随手关闭服务器是个好习惯哦
    s.quit()


if __name__ == '__main__':
    track_price('http://item.jd.com/3212128.html')

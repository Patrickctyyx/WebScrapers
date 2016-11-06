import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver


driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get('http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')
time.sleep(2)

# 点击图书预览按钮
driver.find_element_by_id('sitbLogoImg').click()
imageList = set()

# 等页面加载
time.sleep(5)
# 当右键头可以点开就翻页
while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    # 获取已加载的新页面
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute('src')
        imageList.add(image)

driver.quit()

for image in sorted(imageList):
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen(['tesseract', 'page.jpg', 'page'],
                         # 下面这两行是用来返回文件对象用来发送指令
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.wait()
    f = open('page.txt', 'r')
    print(f.read())

# 用法我都明白，就是没有结果...

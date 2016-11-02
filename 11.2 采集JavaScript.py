from selenium import webdriver
import time


# 这里selenium的参数指明了第三方浏览器的可执行文件路径
# 这里是PhantomJS,相当于一个没有GUI的浏览器
driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
# 这里的选择器比BS直观
print(driver.find_element_by_id('content').text)
driver.close()


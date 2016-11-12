from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/draggableDemo.html')
# 截屏
driver.get_screenshot_as_file('screenshot')

print(driver.find_element_by_id('message').text)

element = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('div2')
# 不知道哪里出错了，好像操作不成功？
actions = ActionChains(driver).drag_and_drop(element, target)
actions.perform()

print(driver.find_element_by_id('message').text)

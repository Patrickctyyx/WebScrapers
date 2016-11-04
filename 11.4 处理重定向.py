#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0
    while True:
        count += 1
        if count > 20:
            print('Timeing out after 10s and returning.')
            return
        time.sleep(0.5)
        # 每五秒检查一下页面还在不在
        try:
            # 如果重定向那么elem和后面的就不相等了
            elem == driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            return

if __name__ == '__main__':
    driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
    driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
    waitForLoad(driver)
    # 出来的界面是重定向后的
    print(driver.page_source)

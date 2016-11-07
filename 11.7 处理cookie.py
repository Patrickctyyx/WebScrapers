from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
savedCookies = driver.get_cookies()

driver2 = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver2.get('http://pythonscraping.com')
driver2.implicitly_wait(1)
driver2.delete_all_cookies()
print(driver2.get_cookies())
for cookie in savedCookies:
    # 这一步有点问题
    # 显示"Can only set Cookies for the current domain"
    # 要改request headers？？？
    driver2.add_cookie(cookie)

driver2.get('http://pythonscraping.com')
print(driver2.get_cookies())

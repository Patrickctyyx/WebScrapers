from selenium import webdriver


# 如果通过了就没提示
# 没通过就报错
driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get('http://en.wikipedia.org/wiki/Kevin_Durant')
# 这不就是系统自带的断言么...
assert 'Kevin Durant' in driver.title
driver.close()

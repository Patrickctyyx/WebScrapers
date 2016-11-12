from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 这里是键盘上的键
from selenium.webdriver import ActionChains


driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/files/form.html')

firstname = driver.find_element_by_name('firstname')
lastname = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

# # Method1
# firstname.send_keys('Patrick')
# lastname.send_keys('Green')
# submitButton.click()

# Method2
# 这里用了ActionChain对象
# 对这个对象可以用点操作符一次执行多个动作
# 最后再到一起perform
actions = ActionChains(driver).click(firstname).send_keys('Tiyanyang')\
                              .click(lastname).send_keys('Cheng')\
                              .send_keys(Keys.RETURN)  # RETURN是回车键
actions.perform()

print(driver.find_element_by_tag_name('body').text)

driver.close()

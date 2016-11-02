from selenium import webdriver
from selenium.webdriver.common.by import By  # 定位器
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 期望条件，触发状态

driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
    # WebDriverWait(driver, 10)这里指定了对象driver，最多等10s
    # 如果有后面的until里面的触发条件就提前触发
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'loadedButton'))  # 这里两重括号不是重复，而是前面那个接受一个tuple为参数
    )
finally:
    print(driver.find_element_by_id('content').text)
    driver.close()

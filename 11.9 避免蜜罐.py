from selenium import webdriver

# 所谓蜜罐就是为了防止黑客，机器人而特地设定的陷阱
# 比如时常会有隐藏的属性，正常用户看不到，而机器人改了值的话
# 就会掉进蜜罐，甚至可能被网站拉黑
driver = webdriver.PhantomJS(executable_path='/home/patrick/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements_by_tag_name('a')
for link in links:
    # link是WebElement对象
    if not link.is_displayed():
        print('The link ' + link.get_attribute('href') + ' is a trap')

fields = driver.find_elements_by_tag_name('input')
for field in fields:
    if not field.is_displayed():
        print('Do not change value of ' + field.get_attribute('name') + ': ' + field.get_attribute('value'))

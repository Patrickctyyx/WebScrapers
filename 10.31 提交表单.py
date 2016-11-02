import requests

# 提交表单时注意字段名称(name属性)，和值
# 并且二者要以dict形式对应
params = {'firstname': 'Patrick', 'lastname': 'Cheng'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=params)
print(r.text)

# 提交文件则需要注意值为文件对象
files = {'uploadFile': open('logo.jpg', 'rb')}
r1 = requests.post('http://pythonscraping.com/pages/processing2.php', files=files)
print(r1.text)

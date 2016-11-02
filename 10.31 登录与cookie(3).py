import requests
from requests.auth import HTTPBasicAuth

# 这里是用HTTP基本接入认证(比较老），而新网站用cookie
auth = HTTPBasicAuth('Patrick', 'password')
r = requests.post('http://pythonscraping.com/pages/auth/login.php', auth=auth)
print(r.text)

import requests

params = {'username': 'Patrick', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(r.cookies.get_dict())  # cookie记录登录状态，这样就不用再次登录
print('----------')
print('Going to profile page..')
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php',
                 cookies=r.cookies)
print(r.text)

import requests

session = requests.session()

params = {'username': 'Patrick', 'password': 'password'}
# session对象记录了所有的会话
# 包括cookie,header，即使变化也会一直捕捉
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('----------')
print('Going to profile page..')
r = session.get('http://pythonscraping.com/pages/cookies/profile.php',
                 cookies=s.cookies)
print(r.text)

import requests
from bs4 import BeautifulSoup


# requests可以改请求头
session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
            (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome\
            /53.0.2785.143 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
url = 'https://www.whatismybrowser.com/'
req = session.get(url, headers=headers)

bsObj = BeautifulSoup(req.text, 'lxml')
print(bsObj.find('a', {'title': 'Your User Agent'}).get_text)

from urllib.request import urlopen
html = urlopen('http://www.jnugeek.cn/static/home.html')
print(html.read())

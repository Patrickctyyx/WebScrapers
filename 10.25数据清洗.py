from urllib.request import urlopen
from bs4 import BeautifulSoup


def ngarms(input_content, n):
    input_content = input_content.split(' ')
    output = []
    for i in range(len(input_content) - n + 1):
        output.append(input_content[i: i + n])
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'lxml')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngarm = ngarms(content, 3)
print(ngarm)
print('3-grams count: ' + str(len(ngarm)))

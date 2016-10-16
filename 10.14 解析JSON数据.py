import json
from urllib.request import urlopen


def getConutry(ip_address):
    response = urlopen('http://freegeoip.net/json/' + ip_address).read().decode('utf-8')
    # json.loads()来解码，把json变成python obj
    # 与此相反，json.dumps()，把python obj变成json
    reponseJSON = json.loads(response)
    return reponseJSON.get('country_code')

print(getConutry('119.29.253.254'))

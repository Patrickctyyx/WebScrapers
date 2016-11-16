import socks
import socket
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, 'localhost', 9150)  # Tor用不了...
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())

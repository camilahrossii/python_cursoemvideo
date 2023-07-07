import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento :(\033[m')
else:
    print('\033[33mConsegui acessar o site Pudim :)\033[m')
    print(site.read())


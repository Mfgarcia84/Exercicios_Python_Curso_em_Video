''''
Crie um código em python que teste se o site pudim está acessível pelo computador usado.
'''

import urllib
import urllib.request
site = str(input("Digite o site: "))
try:
    site1 = urllib.request.urlopen(f"http://{site}")
except urllib.request.URLError:
    print("O site não está acessível no momento")
else:
    print("O site está acessível no momento")
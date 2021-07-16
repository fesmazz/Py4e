import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input("Insira a primeira URL: ")
i = 0
while i < 7 :
    html = urllib.request.urlopen(url).read()
    p_html = BeautifulSoup(html, 'html.parser')
    # encontre todas as Acnhor tags (<a>)
    tags = p_html("a")
    url = (tags[17].get('href', None))
    print(url)
    i += 1

nome = re.findall("^http.+/known_by_(.+).html", url)
print ("O nome procurado é", nome[0])


from urllib.request import urlopen
from bs4 import BeautifulSoup
#import ssl

# Ignore erros de certificado SSL
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1303996.html"
html = urlopen(url).read() #cria uma variável análoga a uma variável "file", que armazena o conteúdo binário sequencial do HTML adquirido pela url
parsedHTML = BeautifulSoup(html, "html.parser")
coments = parsedHTML("span") #cria uma lista com todas as tags <span>

soma = 0
for coment in coments :
    soma += int(coment.contents[0]) #extrai o conteúdo de cada uma das tags span, converte para int e adiciona à variavel soma 
print("Soma:", soma)

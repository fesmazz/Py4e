import urllib.request, urllib.parse, urllib.error
import json

url = input("Insira a URL:")
source = urllib.request.urlopen(url)
data = source.read().decode()
info = json.loads(data) #cria um dicionário a partir das strings em data
soma = 0 
for item in info["comments"]: #para cada item na lista de dicionários armazenada na chave "coments"
    print(item["count"]) #mostre o valor da chave "count"
    soma += int(item["count"]) # adicione este valor à variável soma

print("Soma =", soma)








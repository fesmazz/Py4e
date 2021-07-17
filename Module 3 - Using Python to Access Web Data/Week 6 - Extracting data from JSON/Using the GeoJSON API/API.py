import urllib.request, urllib.parse, urllib.error
import json
endpoint = input("Insira o endpoint da API:")
key = dict()
key["key"] = "42"
key["address"] = input("Insira o endereço desejado:")
url = endpoint + urllib.parse.urlencode(key)
try: addr = urllib.request.urlopen(url)
except: print("URL inválida. Fechando..."); exit()
print("Obtendo informações de", url)
data = addr.read()
print("A resposta da API foi: \n", data.decode())
info = json.loads(data)
print("O \"place_id\" do endereço solicitado é:", info["results"][0]["place_id"])


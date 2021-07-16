import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input ("Insira uma URL: ")
source =  urllib.request.urlopen(url)
data = source.read()
print ("Informações carregadas de", url)
print ("Gostaria de visualizá-las? S/N:")
while True:
    v = input()
    if v == "s" or v == "S" or v == "Y" :
        print (data.decode())
        break
    elif v == "n" or v == "N":
        break
    else:
        print("Gostaria de visualizar os dados? Responda com (S)im ou N(ão)")
        continue
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = 0
for count in counts:
    total += int((count.text))
print("A soma é:", total)






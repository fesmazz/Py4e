import re
source = open("regex_sum_1303994.txt")
numbers_str = list()
for line in source:
   numbers_str.extend(re.findall("[0-9]+", line)) #extrai qualquer sequencia de dígitos entre 0 e 9 e armazena como strings na lista numbers_str
numbers_int = [int(i) for i in numbers_str] #converte todos os valores da lista numbers_str para int
print(sum(numbers_int))


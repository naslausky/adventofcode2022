# Desafio do dia 01/12/2022:
#a) Receber uma lista de listas de números, e ver qual delas tem a maior soma.
#b) Somar as três listas de maior soma.

with open ("input.txt") as file:
	elfos = file.read().split('\n\n')

caloriasTotais = []
for elfo in elfos:
	calorias = elfo.splitlines()
	calorias = list(map(int, calorias))
	soma = sum(calorias)
	caloriasTotais.append(soma)

caloriasTotais.sort()
print('Soma do elfo com mais calorias:', caloriasTotais[-1])
print('Soma dos três elfos com mais calorias:', sum(caloriasTotais[-3:]))

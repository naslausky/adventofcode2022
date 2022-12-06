# Desafio do dia 06/12/2022:
# a) Receber uma string e calcular o índice em que 4 caracteres distintos seguidos aparecem.
# b) Idem, porém para 14 caracteres.

with open('input.txt') as file:
	linha = file.read()

for indice in range(len(linha)):
	caracteres = linha[indice : indice + 4]
	conjunto = {c for c in caracteres}
	if len(conjunto) == 4:
		print('Índice que ocorrem 4 caracteres distintos:', indice + 4)
		break

# Parte 2:
for indice in range(len(linha)):
	caracteres = linha[indice : indice + 14]
	conjunto = {c for c in caracteres}
	if len(conjunto) == 14:
		print('Índice que ocorrem 14 caracteres distintos:', indice + 14)
		break

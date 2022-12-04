# Desafio do dia 04/12/2022:
# a) Receber uma lista de pares de intervalos, e calcular quantos desses pares tem um intervalo que contém o outro.
# b) Na mesma lista, contar quantos pares tem algum elemento em comum.

with open('input.txt') as file:
	linhas = file.read().splitlines()

resposta = 0
respostaParte2 = 0
for linha in linhas:
	intervalo1, intervalo2 = linha.split(',')
	intervalo1 = intervalo1.split('-')
	intervalo1 = list(map(int, intervalo1))
	intervalo2 = intervalo2.split('-')
	intervalo2 = list(map(int, intervalo2))
	conjunto1 = {elemento for elemento in range(intervalo1[0], intervalo1[1] + 1)}
	conjunto2 = {elemento for elemento in range(intervalo2[0], intervalo2[1] + 1)}

	if conjunto1.issubset(conjunto2) or conjunto2.issubset(conjunto1):
		resposta += 1 # Verifica se um contém o outro.
	if len(conjunto1.intersection(conjunto2)) > 0:
		respostaParte2 += 1 # Se existe alguma sobreposição, a interseção não é nula.

print('A quantidade de pares que um contém o outro é:', resposta)
print('A quantidade de pares que tem alguma sobreposição é:', respostaParte2)

# Desafio do dia 03/12/2022:
#a) Receber uma lista de strings, e calcular o valor dos caracteres comuns entre a primeira e segunda metade de cada.
#b) Calcular o valor do caracter comum entre 3 strings seguidas.

with open ("input.txt") as file:
	linhas = file.read().splitlines()
resposta = 0
for linha in linhas:
	tamanho = int(len(linha)/2)
	primeiraMetade = linha[:tamanho]
	segundaMetade = linha[tamanho:]
	elementosEmComum = {letra for letra in primeiraMetade if letra in segundaMetade}
	pontuacao = sum([ord(letra) - (96 if letra.islower() else 38) for letra in elementosEmComum])
	resposta += pontuacao
print('A pontuação dos elementos em comum entre as metades é:', resposta)

# Parte 2:
resposta = 0
for indice in range(int(len(linhas) / 3)):
	linha1 = linhas[indice * 3 + 0]
	linha2 = linhas[indice * 3 + 1]
	linha3 = linhas[indice * 3 + 2]
	elementosEmComum = {letra for letra in linha1 if letra in linha2 and letra in linha3}
	pontuacao = sum([ord(letra) - (96 if letra.islower() else 38) for letra in elementosEmComum])
	resposta += pontuacao
print('A pontuação dos elementos em comum a cada três linhas é:', resposta)

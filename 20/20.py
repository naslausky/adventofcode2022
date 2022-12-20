with open('input.txt') as file:
	linhas = file.read().splitlines()
	numeros = list(map(int, linhas))

class No:
	def __init__(self, numero):
		self.numero = numero
		self.anterior = None
		self.proximo = None
# Gerando os nós:
primeiroNo = No(numeros[0])
nosDosNumeros = {0 : primeiroNo}
noAnterior = primeiroNo
for indice, numero in enumerate(numeros[1:]):
	noDesseNumero = No(numero)
	nosDosNumeros[indice + 1] = noDesseNumero
	noAnterior.proximo = noDesseNumero
	noDesseNumero.anterior = noAnterior
	noAnterior = noDesseNumero	
primeiroNo.anterior = noAnterior
noAnterior.proximo = primeiroNo

#def imprimirLista(no):
#	noAtual = no.proximo
#	resposta = [0]
#	while noAtual != no:
#		resposta.append(noAtual.numero)
#		noAtual=noAtual.proximo
#	print(resposta)

for indice, numero in enumerate(numeros):	
	if numero == 0:
		continue
	primeiroNo = nosDosNumeros[indice]
	segundoNo = primeiroNo

	for _ in range(abs(primeiroNo.numero)):
		if primeiroNo.numero > 0:
			segundoNo = segundoNo.proximo
		else:
			segundoNo = segundoNo.anterior
	if primeiroNo.numero < 0:
		segundoNo = segundoNo.anterior
	primeiroNo.anterior.proximo = primeiroNo.proximo
	primeiroNo.proximo.anterior = primeiroNo.anterior

	segundoNo.proximo.anterior = primeiroNo
	primeiroNo.proximo = segundoNo.proximo

	segundoNo.proximo = primeiroNo
	primeiroNo.anterior = segundoNo

noAtual = nosDosNumeros[numeros.index(0)]
resposta = 0
for _ in range(3):
	for indice in range(1000):
		noAtual = noAtual.proximo
	resposta += noAtual.numero
print(resposta)



#parte 2:
chaveDeDecodificacao = 811589153
numeros = [numero * chaveDeDecodificacao for numero in numeros]

# Gerando os nós:
primeiroNo = No(numeros[0])
nosDosNumeros = {0 : primeiroNo}
noAnterior = primeiroNo
for indice, numero in enumerate(numeros[1:]):
	noDesseNumero = No(numero)
	nosDosNumeros[indice + 1] = noDesseNumero
	noAnterior.proximo = noDesseNumero
	noDesseNumero.anterior = noAnterior
	noAnterior = noDesseNumero	
primeiroNo.anterior = noAnterior
noAnterior.proximo = primeiroNo
for _ in range(10):
	# Misturando:
	for indice, numero in enumerate(numeros):	
		if numero == 0:
			continue
		primeiroNo = nosDosNumeros[indice]
		segundoNo = primeiroNo
		vezesARodar = abs(primeiroNo.numero) % (len(numeros)-1)
		for _ in range(vezesARodar):
			if primeiroNo.numero > 0:
				segundoNo = segundoNo.proximo
			else:
				segundoNo = segundoNo.anterior
		if primeiroNo.numero < 0:
			segundoNo = segundoNo.anterior
		primeiroNo.anterior.proximo = primeiroNo.proximo
		primeiroNo.proximo.anterior = primeiroNo.anterior

		segundoNo.proximo.anterior = primeiroNo
		primeiroNo.proximo = segundoNo.proximo

		segundoNo.proximo = primeiroNo
		primeiroNo.anterior = segundoNo

noAtual = nosDosNumeros[numeros.index(0)]
resposta = 0
for _ in range(3):
	for indice in range(1000):
		noAtual = noAtual.proximo
	print('incrementando', noAtual.numero)
	resposta += noAtual.numero
print(resposta)

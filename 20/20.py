# Desafio do dia 20/12/2022:
# a) Dada uma lista circular de números, mover cada número baseado em seu valor. Calcular o estado final da lista.
# b) Idem, porém multiplicar cada item da lista por uma constante, e fazer a operação de mover 10 vezes.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	numeros = list(map(int, linhas))

class No: # Representa um nó na lista. Contém o número em si, e uma referência ao próximo elemento da lista.
	def __init__(self, numero):
		self.numero = numero
		self.anterior = None
		self.proximo = None

def gerarNos(): # Gerar os nós e as ligações:
	primeiroNo = No(numeros[0]) # Armazena a referência ao primeiro nó para fechar o círculo ao final.
	nosDosNumeros = {0 : primeiroNo} # Dicionário que relaciona cada elemento da lista de números original ao seu nó.
	noAnterior = primeiroNo
	for indice, numero in enumerate(numeros[1:]):
		noDesseNumero = No(numero)
		nosDosNumeros[indice + 1] = noDesseNumero
		noAnterior.proximo = noDesseNumero
		noDesseNumero.anterior = noAnterior
		noAnterior = noDesseNumero	
	primeiroNo.anterior = noAnterior
	noAnterior.proximo = primeiroNo
	return primeiroNo, nosDosNumeros

def misturar(): # Função que realiza uma mistura dos elementos dos números baseado no valor de cada um.
	for indice, numero in enumerate(numeros):	
		if numero == 0: # Não existe modificação na lista.
			continue
		primeiroNo = nosDosNumeros[indice] # Nó origem.
		segundoNo = primeiroNo
		vezesARodar = abs(primeiroNo.numero) % (len(numeros) - 1)
		if primeiroNo.numero < 0:
			vezesARodar += 1 # Para pegar sempre o número a esquerda de onde se deseja inserir.
		for _ in range(vezesARodar):
			if primeiroNo.numero > 0:
				segundoNo = segundoNo.proximo
			else:
				segundoNo = segundoNo.anterior
		primeiroNo.anterior.proximo = primeiroNo.proximo # Remove o nó de onde está:
		primeiroNo.proximo.anterior = primeiroNo.anterior

		segundoNo.proximo.anterior = primeiroNo # Insere ele na posição nova:
		primeiroNo.proximo = segundoNo.proximo

		segundoNo.proximo = primeiroNo
		primeiroNo.anterior = segundoNo

def resposta(): # Função que percorre a lista e calcula a resposta somando os elementos de índice 1000, 2000 e 3000.
	noAtual = nosDosNumeros[numeros.index(0)]
	resposta = 0
	for _ in range(3):
		for indice in range(1000):
			noAtual = noAtual.proximo
		resposta += noAtual.numero
	return resposta

primeiroNo, nosDosNumeros = gerarNos()
misturar()
print('A soma das coordenadas descriptografadas do bosque é:', resposta())

# Parte 2:
chaveDeDecodificacao = 811589153
numeros = [numero * chaveDeDecodificacao for numero in numeros]
primeiroNo, nosDosNumeros = gerarNos()
for _ in range(10): # Fazer a mistura dez vezes.
	misturar()
print('A soma das coordenadas descriptografadas do bosque após as 10 misturas é:', resposta())

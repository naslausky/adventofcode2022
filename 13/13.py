# Desafio do dia 13/12/2022:
# a) Receber uma lista de pares de listas, e uma regra de ordem. 
#    Baseado nesta regra, verificar quais estão ordenados corretamente.
# b) Ordenar todos os pares e verificar em qual índice ficam dois pares específicos.

import functools
with open('input.txt') as file:
	pares = file.read().split('\n\n')

def comparar(esquerda, direita): # Função que retorna 1, 0 ou -1 baseado nos dois elementos passados.
	if type(esquerda) is int and type(direita) is int:
		if esquerda < direita:
			return 1
		elif esquerda > direita:
			return -1
		else:
			return 0
	
	if type(esquerda) is int: # Se chegou aqui é porque no mínimo um dos dois é uma lista.
		esquerda = [esquerda]

	if type(direita) is int:
		direita = [direita]

	if type(esquerda) is list and type(direita) is list:
		intervalo = min(len(esquerda), len(direita)) # Compara até o final da menor das listas.
		for indice in range(intervalo):
			resultado = comparar(esquerda[indice], direita[indice])
			if resultado != 0:
				return resultado

		if len(esquerda) < len (direita):
			return 1
		elif len(esquerda) > len(direita):
			return - 1
		else:
			return 0
		
todosOsPares = [] # Lista completa para ordenação usada na parte 2.
somaIndices = 0 # Resposta da parte 1.
for indicePar, par in enumerate(pares):
	indicePar += 1 # O primeiro par tem índice 1.
	par = par.splitlines()
	esquerda = eval(par[0])
	direita = eval(par[1])
	todosOsPares.extend([esquerda, direita]) # Popula a lista completa para a parte 2.
	if comparar(esquerda, direita) == 1:
		somaIndices += indicePar
print('A soma dos índices dos pares ordenados corretamente é:', somaIndices)
# Parte 2:
divisor1, divisor2 = [[2]], [[6]] # Novas listas a serem adicionadas para parte 2.
todosOsPares.append(divisor1)
todosOsPares.append(divisor2)
todosOsPares.sort(key = functools.cmp_to_key(comparar), reverse = True)
chaveDecodificacao = 1 # Resposta da parte 2.
for indicePar, par in enumerate(todosOsPares):
	if par == divisor1 or par == divisor2:
		chaveDecodificacao *= indicePar + 1
print('O produto dos índices das listas adicionadas após ordenação é:', chaveDecodificacao)

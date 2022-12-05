# Desafio do dia 05/12/2022:
# a) Receber uma lista de pilhas de caixas, e uma serie de remanejamentos. Calcular qual caixa vai estar em cima de cada pilha ao final. 
# b) Idem, porém onde cada movimento pode levar múltiplas caixas.

with open('input.txt') as file:
	caixas, ordens = file.read().split('\n\n')
	ordens = ordens.splitlines()
	caixas = caixas.splitlines()

ultimaLinha = caixas[-1] # Linha com o "nomes" de cada pilha.
indices = {int(indice) : ultimaLinha.index(indice) for indice in ultimaLinha.split()}
pilhas = {indice : '' for indice in indices} # Dicionário que vai relacionar o índice de uma pilha, ao seu conteúdo. Da forma: {1: 'ABC'}

for numeroCaixa, indice in indices.items():
	for linha in reversed(caixas[:-1]):
		if linha[indice] != ' ':
			pilhas[numeroCaixa] += linha[indice]
pilhasParte2 = pilhas.copy()

def mover(qtd, origem, destino, pilhas, multiplos = False):
	caixasRemovidas = pilhas[origem][-qtd:]
	if not multiplos:
		caixasRemovidas = caixasRemovidas[::-1] # Inverte a ordem para a primeira parte.
	pilhas[origem] = pilhas[origem][:-qtd]
	pilhas[destino] += caixasRemovidas

for ordem in ordens:
	palavras = ordem.split()
	qtd, origem, destino = palavras[1], palavras[3], palavras[5]
	qtd, origem, destino = list(map(int, [qtd, origem, destino]))
	mover(qtd, origem, destino, pilhas, multiplos = False)
	mover(qtd, origem, destino, pilhasParte2, multiplos = True)
resposta = ''.join([x[-1] for x in pilhas.values()])
respostaParte2 = ''.join([x[-1] for x in pilhasParte2.values()])

print('As caixas superiores podendo mover apenas uma caixa por vez são:', resposta)
print('As caixas superiores podendo mover múltiplas caixas são:', respostaParte2)

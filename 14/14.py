# Desafio do dia 14/12/2022:
# a) Receber uma lista de paredes e uma fonte de areia infinita e calcular quantas coordenadas serão alcançadas pela areia.
# b) Idem, porém agora com um chão extra abaixo.

with open('input.txt') as file:
	linhas = file.read().splitlines()

mapa = {} # Dicionário que relaciona cada coordenada a seu conteúdo ('#' ou 'o').
for linha in linhas:
	pontos = linha.split(' -> ')
	for indicePonto in range(len(pontos) - 1):
		ponto1, ponto2 = pontos[indicePonto], pontos[indicePonto + 1]
		ponto1 = list(map(int, ponto1.split(',')))
		ponto2 = list(map(int, ponto2.split(',')))
		coordenadaAtual = ponto1
		chave = tuple(coordenadaAtual)
		destino = tuple(ponto2)
		mapa[chave] = '#'
		while tuple(coordenadaAtual) != destino:
			for dimensao in range(2):
				if coordenadaAtual[dimensao] != destino[dimensao]:
					coordenadaAtual[dimensao] += 1 if coordenadaAtual[dimensao] < destino[dimensao] else -1
			chave = tuple(coordenadaAtual)
			mapa[chave] = '#'
maiorProfundidade = max(mapa, key = lambda x: x[1])[1]

def cair1Areia(): # Função que insere um grão de areia e retorna se verdadeiro se inseriu com sucesso
# ou falso caso tenha passado da coordenada limite, ou se o grão foi posto na origem (e tampou a fonte).
	coordenadaAtual = (500 , 0)
	while (True):
		if coordenadaAtual[1] > maiorProfundidade:
			return False
		abaixo = (coordenadaAtual[0], coordenadaAtual[1] + 1)
		diagonalEsquerda = (coordenadaAtual[0] - 1, coordenadaAtual[1] + 1)
		diagonalDireita = (coordenadaAtual[0] + 1, coordenadaAtual[1] + 1)
		candidatosADestino = (abaixo, diagonalEsquerda, diagonalDireita)
		for candidato in candidatosADestino: # Boa oportunidade para usar for / else.
			if candidato not in mapa:
				coordenadaAtual = candidato
				break
		else: # Caso não tenha achado um destino, fica onde está.
			mapa[coordenadaAtual] = 'o'
			return coordenadaAtual != (500, 0) # Sempre retorna verdadeiro, porém na parte 2 acaba quando chegar na coordenada de origem.
while(cair1Areia()): # Preenche com areia até não poder mais.
	pass
print('O número de grãos de areia dispostos é:', sum([1 for x, y in mapa.items() if y == 'o']))

# Parte 2:
maiorProfundidade += 2
for indiceHorizontal in range (500 - maiorProfundidade - 2, 500 + maiorProfundidade + 2):
	mapa[(indiceHorizontal, maiorProfundidade)] = '#' # Preenche com um "chão" de largura suficiente para um triângulo se formar.
while(cair1Areia()): # Continua a preencher o mesmo mapa, agora com o segmento extra.
	pass
print('O número de grãos de areia dispostos com o segmento extra é:', sum([1 for x, y in mapa.items() if y == 'o']))

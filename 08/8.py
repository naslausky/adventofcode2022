# Desafio do dia 08/12/2022:
# a) Receber uma matriz de números representando alturas. Calcular quantas coordenadas são visíveis por alguma borda.
# b) Calcular qual a coordenada interna que vê o maior número de outras coordenadas.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	quantidadeDeLinhas = len(linhas)
	quantidadeColunas = len(linhas[0])

arvores = {} # Dicionário que relaciona uma coordenada a sua altura.
for indiceLinha, linha in enumerate(linhas):
	for indiceCaracter, alturaArvore in enumerate(linha):
		coordenada = (indiceLinha, indiceCaracter)
		arvores[coordenada] = int(alturaArvore)

quantidadeDeArvoresVisiveis = 0
maiorPontuacao = 0
for indiceLinha in range(quantidadeDeLinhas):
	for indiceCaracter in range(quantidadeColunas): # Para cada árvore.
		alturaDestaArvore = arvores[(indiceLinha, indiceCaracter)]
		visivel = False # Representa se a árvore é visível por alguma direção.
		pontuacao = 1
		intervalos = ( # Representa todos os intervalos que deve-se olhar partindo desta árvore.
						reversed(range(0, indiceCaracter)),	# Esquerda.
						range(indiceCaracter + 1, quantidadeColunas), # Direita.
						reversed(range(0, indiceLinha)), # Cima.
						range(indiceLinha + 1, quantidadeDeLinhas)) # Baixo.

		for indiceIntervalo, intervalo in enumerate(intervalos): # Para cada uma das quatro direções:
			ehVisivelNestaDirecao = True
			arvoresVistasNestaDirecao = 0
			for indiceCoordenada in intervalo: # Verificar todas as árvores vistas nesta direção.
				# O eixo que varia depende de qual intervalo estamos. Os dois primeiros são horizontais.
				chave = ( (indiceLinha, indiceCoordenada) if indiceIntervalo < 2 else 
						  (indiceCoordenada, indiceCaracter))
				arvoresVistasNestaDirecao += 1
				if arvores[chave]  >= alturaDestaArvore:
					ehVisivelNestaDirecao = False
					break
			pontuacao *= arvoresVistasNestaDirecao
			visivel = visivel or ehVisivelNestaDirecao # Basta ser visível por uma direção.
		
		if visivel:
			quantidadeDeArvoresVisiveis += 1
		maiorPontuacao = max(maiorPontuacao, pontuacao)

print('A quantidade de árvores que são vistas de fora da floresta é:', quantidadeDeArvoresVisiveis)
print('A maior pontuação dentre todas as árvores é:', maiorPontuacao)

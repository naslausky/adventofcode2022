# Desafio do dia 12/12/2022:
# a) Receber um mapa de alturas, e calcular a distância mínima entre a origem e o destino, onde cada passo pode subir ao máximo um nível.
# b) Calcular a menor distância entre todas as origens possíveis.

with open('input.txt') as file:
	linhas = file.read().splitlines()

mapa = {} # Mapa que relaciona uma coordenada a sua altura.
for indiceLinha, linha in enumerate(linhas):
	for indiceCaracter, caracter in enumerate(linha):
		coordenada = (indiceLinha, indiceCaracter)
		if caracter == 'S':
			origem = coordenada
			mapa[coordenada] = 0
		elif caracter == 'E':
			destino = coordenada
			mapa[coordenada] = ord('z') - ord('a')
		else:
			mapa[coordenada] = ord(caracter) - ord('a')

vistos = set() # Coordenadas que já foram avaliadas.
distancias = {destino: 0} # Mapa que relaciona a menor distância conhecida até agora para cada destino.

while len(vistos) != len(distancias): # Enquanto ainda houverem coordenadas a serem verificadas.
	conhecidosNaoVistos = {chave : valor for chave, valor in distancias.items() if chave not in vistos}
	menorConhecidoNaoVisto = min(conhecidosNaoVistos, key = conhecidosNaoVistos.get)
	distanciaAteAqui = distancias[menorConhecidoNaoVisto]
	lados = ((0, 1), (0, -1), (1, 0), (-1, 0))
	x, y = menorConhecidoNaoVisto
	for lado in lados:
		coordenadaLateral = (lado[0] + x, lado[1] + y)
		if coordenadaLateral not in mapa: continue
		# Como a parte 2 pede para múltiplas origens, 
		# é mais simples popular as distâncias tendo a origem sendo o final, 
		# e verificar as distâncias para cada origem possível. Assim o Dijkstra feito apenas uma vez.
		# Nesse caso, a desigualdade deve ser invertida (cada coordenada só pode descer no máximo 1).
		if mapa[coordenadaLateral] >= mapa[menorConhecidoNaoVisto] - 1: # É um destino possível.
			if coordenadaLateral not in distancias or distancias[coordenadaLateral] > distanciaAteAqui + 1:
				distancias[coordenadaLateral] = distanciaAteAqui + 1
	vistos.add(menorConhecidoNaoVisto)

origensPossiveis = [chave for chave in mapa if mapa[chave] == 0] # Todas as coordenadas com altura zero.
menoresDistancias = [distancias[coordenada] for coordenada in origensPossiveis if coordenada in distancias]
print('A menor distância entre a origem e o destino é:', distancias[origem])
print('A menor distância entre os candidatos de origem e o destino é:', min(menoresDistancias))

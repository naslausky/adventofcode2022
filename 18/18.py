# Desafio do dia 18/12/2022:
# a) Dada uma lista de pontos representando centros de cubos 1x1x1, calcular a área da superfície.
# b) Idem, porém contabilizar apenas paredes que são alcançáveis pela parte externa.

with open('input.txt') as file:
	pontos = file.read().splitlines()
cubo = ( 	# São as coordenadas de um cubo centrado em 0,0,0.
			# São 6 lados, onde cada lado é um conjunto de 4 pontos.
			# A ordem dos 6 lados precisa ser essa para coincidir com os destinos da parte 2.
((1,0,0), (1,1,0), (1,1,1), (1,0,1)), # X + 1.
((0,0,0), (0,1,0), (0,1,1), (0,0,1)), # X - 1.
((1,1,0), (0,1,0), (1,1,1), (0,1,1)), # Y + 1.
((0,0,0), (1,0,0), (0,0,1), (1,0,1)), # Y - 1.
((0,0,1), (1,0,1), (1,1,1), (0,1,1)), # Z + 1.
((0,0,0), (1,0,0), (1,1,0), (0,1,0))  # Z - 1.
)

maiores = [0,0,0] # Usado na parte 2 para restringir a busca. Poderia-se fazer uma lista "menores" também.
lados = {}
for ponto in pontos:
	ponto = ponto.split(',')
	ponto = tuple(map(int, ponto))
	for lado in cubo:
		coordenadasDesteLado = []
		for canto in lado:
			pontoConvertido = (
				ponto[0] + canto[0],
				ponto[1] + canto[1],
				ponto[2] + canto[2],
			)
			for dimensao in range(3): # Armazena para a parte 2 os maiores índices em cada dimensão.
				maiores[dimensao] = max(maiores[dimensao], pontoConvertido[dimensao])
			coordenadasDesteLado.append(pontoConvertido)
		coordenadasDesteLado.sort()
		coordenadasDesteLado = tuple(coordenadasDesteLado) 
		# Uma parede é unicamente identificada como coordenadas de 4 pontos *ordenados*.
		# Contabiliza quantas vezes essa parede existe:
		lados[coordenadasDesteLado] = 1 + lados.get(coordenadasDesteLado, 0)
ladosSemSobreposicao = {lado for lado, quantidade in lados.items() if quantidade == 1}
print('A área total da superfície:', len(ladosSemSobreposicao))

# Parte 2:
# Partindo de um ponto bem externo, verificar quais são alcançáveis.
origem = (maiores[0] + 1, maiores[1] + 1, maiores[2] + 1) 
vistos = set()
distancias = {origem : 0}
# Quando o algoritmo não conseguir alcançar em uma dimensão, é porque ele bateu em uma parede, logo ela é visível e deve ser contabilizada para a resposta:
paredesVisiveis = set()

while len(vistos) != len(distancias):
	conhecidosNaoVistos = {chave: valor for chave, valor in distancias.items() if chave not in vistos}
	menorConhecidoNaoVisto = min(conhecidosNaoVistos, key = distancias.get)	
	distanciaAteAqui = distancias[menorConhecidoNaoVisto]
	proximosCubos = [] # Potenciais 6 destinos:
	for dimensao in range(3): # Para cada eixo, existe um potencial destino acima e outro abaixo.
		proximoDestino = list(menorConhecidoNaoVisto)
		proximoDestino[dimensao] += 1
		proximosCubos.append(tuple(proximoDestino))
		proximoDestino[dimensao] -= 2
		proximosCubos.append(tuple(proximoDestino))
	# Desses 6, verificar quais são alcançáveis. Ele não é alcançável se:
	# ) Tiver uma parede obstruindo o caminho.
 	# ) Estiver fora do escopo da busca (fora do range do input).
	for indice, destino in enumerate(proximosCubos): # Para cada um dos 6 possiveis destinos:
		alcancavel = True # Verificar se ele é alcançável.
		lado = cubo[indice] # Para esse destino especifico, é esse lado. 
		# A ordem que a constante cubo foi escrita é proposital para coincidir com os indices de destinos possíveis.
		coordenadasDesteLado = []
		for canto in lado: # Obtem a tupla do lado que é necessário atravessar para ir para esse destino.
			pontoConvertido = (
				menorConhecidoNaoVisto[0] + canto[0],
				menorConhecidoNaoVisto[1] + canto[1],
				menorConhecidoNaoVisto[2] + canto[2],
			)
			for dimensao in range(3):
				if (pontoConvertido[dimensao] > maiores[dimensao] + 2) or (pontoConvertido[dimensao] < -1):
					alcancavel = False # Fora do escopo da busca.
			coordenadasDesteLado.append(pontoConvertido)
		coordenadasDesteLado.sort()
		coordenadasDesteLado = tuple(coordenadasDesteLado)
		if coordenadasDesteLado in ladosSemSobreposicao: # Há uma parede na frente, logo não é um destino.
			paredesVisiveis.add(coordenadasDesteLado) # É uma parede visível do exterior.
			alcancavel = False # Não se pode caminhar para lá.
		if not alcancavel:
			continue # Não adicionar esse destino como um próximo ponto a se verificar.
		distancias[destino] = min(distanciaAteAqui + 1, distancias.get(destino, 999))
	vistos.add(menorConhecidoNaoVisto)
print('A área da superfície visível pelo exterior é:', len(paredesVisiveis))

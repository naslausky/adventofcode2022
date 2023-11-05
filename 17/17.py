with open('input.txt') as file:
	linha = file.read().splitlines()[0]

pedras = ( # Os 5 tipos de pedras existentes.
((2,3),(3,3),(4,3),(5,3)),
((3, 5),(3, 4),(3,3),(2,4),(4,4)),
((2,3),(3,3),(4,3),(4,4),(4,5)),
((2,3),(2,4),(2,5),(2,6)),
((2,3),(2,4),(3,3),(3,4))
)

mapa = {} # Mapa que contém as coordenadas que contém um pedaço de pedra. Deve poder mudar pra set.
for x in range(7): # Inicializar com o primeiro "chão".
	mapa[(x, -1)] = None
menorAlturaSemPedra = 0 # Altura da coluna mais alta da torre.
alturaDoChaoMaisAlto = -1 # Quando um andar inteiro fica preenchido, é um chão.
indiceJato = 0 # Índice do caracter do meu input.
gabarito = {} # Mapa associa um estado com o índice da pedra atual. Usado para achar um "ciclo" e economizar iterações.

def imprimirMapa(pedraAtual = ()): # Função de depuração que imprime os 20 andares mais altos do mapa.
	menorAlturaSemPedra = max(mapa, key= lambda x:x[1])[1] + 1
	for indiceLinha in reversed(range(menorAlturaSemPedra-20, menorAlturaSemPedra)):
		print(''.join('#' if ((indiceCaracter, indiceLinha) in mapa or 
								(indiceCaracter, indiceLinha) in pedraAtual)
				else '.' for indiceCaracter in range(7)))

objetivoAtual = 2022 # Número de iterações da parte 1.
objetivoSeguinte = 1000000000000 # Número de iterações da parte 2.
indicePedra = 0 # É o que vai ser verificado com o objetivo.
while (indicePedra < objetivoAtual): # Cada iteração desse while é uma pedra caindo por completo.
	tipoPedra = indicePedra % len(pedras) # Se é horizontal, em cruz, em L...
	pedraAtual = [list(coordenada) for coordenada in pedras[tipoPedra]] # Lista para poder ir movendo aos poucos.
	for coordenada in pedraAtual: # Começa 3 acima da maior altura da torre. O mapa "pedras" já tem as coordenadas transladadas de +3:
		coordenada[1]+= menorAlturaSemPedra
	while (True): # Vai movendo a pedra para o lado, e pra baixo:
		lado = linha[indiceJato % len(linha)] # Caracter indicando direita ou esquerda.
		indiceJato = (indiceJato + 1) % len(linha)
		direita = lado == '>'
		# Se tentar ir para esquerda, verifica a parede esquerda (menor X), senão a direita (maior X).
		coordenadaASeVerificarColisao = max(pedraAtual)[0] if direita else min(pedraAtual)[0] 
		podeMexer = coordenadaASeVerificarColisao < 6 if direita else coordenadaASeVerificarColisao > 0
		if podeMexer:
			todasAsCoordenadasPodemMover = True
			delta = 1 if direita else -1
			for coordenada in pedraAtual: # Verifica para todos os pontos se tem alguma pedra obstruindo o lado.
					coordenadaLateral = (coordenada[0] + delta, coordenada[1])
					if coordenadaLateral in mapa: # Alguma delas não dá pra ir pra direita.
						todasAsCoordenadasPodemMover = False
			if todasAsCoordenadasPodemMover:
				for coordenada in pedraAtual:
					coordenada[0] += delta					
		daPraDescer = True
		for coordenada in pedraAtual:
			coordenadaInferior = (coordenada[0], coordenada[1] - 1)
			if coordenadaInferior in mapa: # Alguma delas não dá pra descer mais.
				daPraDescer = False
		if daPraDescer: # Todas as coordenadas podem descer. Descer 1 andar em todas.
			for coordenada in pedraAtual:
				coordenada[1] -= 1
		else: # A pedra estabilizou no fundo.
			maiorY = 0 # Pode usar o max diretamente com a lambda.
			for coordenada in pedraAtual: # Adiciona a pedra já estabilizada no mapa.
				maiorY = max(coordenada[1], maiorY)
				mapa[tuple(coordenada)] = None
				oChaoFechou = True # Verificar se o chão fechou uma linha completa:
				alturaDestaCoordenada = coordenada[1]
				for x in range(7):
					if (x, alturaDestaCoordenada) not in mapa:
						oChaoFechou = False
				if oChaoFechou: # Atualiza com o potencial novo chão mais alto.
					alturaDoChaoMaisAlto = max(alturaDoChaoMaisAlto, alturaDestaCoordenada)
			menorAlturaSemPedra = max(menorAlturaSemPedra, maiorY + 1) # Atualiza com a nova altura máxima da torre.
			
			# Limpar o que tiver abaixo do chão mais alto:
			mapa = {chave: valor for chave, valor in mapa.items() if chave[1]>=alturaDoChaoMaisAlto}
			
			numeros = [] # Gera o estado para salvar no gabarito:
			for indiceColuna in range(7): # Para cada pilastra do mapa.
				numeroDestaColuna = '' # Gera um número binário representando o estado desta pilastra.
				for altura in range(alturaDoChaoMaisAlto, menorAlturaSemPedra):
					numeroDestaColuna += '1' if (indiceColuna, altura) in mapa else '0'
				numeros.append(int(numeroDestaColuna, 2))
				
			numeros.append(indiceJato) # Também faz parte do estado o índice em nosso input,
			numeros.append(tipoPedra) # e o tipo da pedra que estabilizou.
			chaveParaSalvarNoGabarito = tuple(numeros)
			if (chaveParaSalvarNoGabarito) in gabarito: # Este estado repetiu.
				periodoParaRepetir = indicePedra - gabarito[chaveParaSalvarNoGabarito][0] # Verificar a diferença entre iterações
				quantoFaltaParaTerminar = objetivoAtual - indicePedra # ... e pular o máximo possível de iterações.
				if periodoParaRepetir != 0: 
					quantosPassosPossoPular = quantoFaltaParaTerminar // periodoParaRepetir
					indicePedra += (quantosPassosPossoPular * periodoParaRepetir)
					# Atualizar as alturas do mapa com os N pulos de ciclo que fizemos.
					distanciaQueSubiuEm1Periodo = alturaDoChaoMaisAlto - gabarito[chaveParaSalvarNoGabarito][1]
					alturaASubir = quantosPassosPossoPular * distanciaQueSubiuEm1Periodo
					mapa = {(chave[0], chave[1] + alturaASubir) : valor for chave, valor in mapa.items()}
					alturaDoChaoMaisAlto += alturaASubir
					menorAlturaSemPedra += alturaASubir			
			else: # O estado não repetiu, salvar no gabarito para conferir no futuro.
				gabarito[chaveParaSalvarNoGabarito] = (indicePedra, alturaDoChaoMaisAlto)
				
			if (indicePedra == objetivoAtual-1): # Verifica se chegou ao objetivo.
				print('Altura da torre após', objetivoAtual, 'pedras:', menorAlturaSemPedra)
				if (objetivoAtual != objetivoSeguinte): # Atualiza para o objetivo da parte 2.
					objetivoAtual = objetivoSeguinte
			break # Acabou esta iteração de pedra.
	indicePedra += 1

with open('input.txt') as file:
	linha = file.read().splitlines()[0]

pedras = ( # Os 5 tipos de pedras existentes.
((2,3),(3,3),(4,3),(5,3)),
((3, 5),(3, 4),(3,3),(2,4),(4,4)),
((2,3),(3,3),(4,3),(4,4),(4,5)),
((2,3),(2,4),(2,5),(2,6)),
((2,3),(2,4),(3,3),(3,4))
)

#Cria o mapa.
mapa = {}
for x in range(7): # Inicializa com o "chão":
	mapa[(x, -1)] = None
menorAlturaSemPedra = 0 # Altura da coluna mais alta da torre.
alturaDoChaoMaisAlto = -1
indiceJato = 0 # Indice do caracter do meu input.

gabarito = {}

def imprimirMapa(pedraAtual = ()):
	menorAlturaSemPedra = max(mapa, key= lambda x:x[1])[1] + 1
	for indiceLinha in reversed(range(menorAlturaSemPedra-20, menorAlturaSemPedra)):
		print(''.join('#' if ((indiceCaracter, indiceLinha) in mapa or 
								(indiceCaracter, indiceLinha) in pedraAtual)
				else '.' for indiceCaracter in range(7)))

objetivoAtual = 2022
objetivoSeguinte = 1000000000000
indicePedra = 0
while (True):
	#print('Comecando Pedra', indicePedra)
	#Cair uma pedra até o final.
	tipoPedra = indicePedra % len(pedras)
	#Inserir a pedra:
	pedraAtual = [list(coordenada) for coordenada in pedras[tipoPedra]]
	#imprimirMapa()
	#input()
	#Coloca na altura correta:
	for coordenada in pedraAtual:
		coordenada[1]+= menorAlturaSemPedra
	while (True):
		# Vai movendo a pedra para o lado, e pra baixo:
		lado = linha[indiceJato % len(linha)] # Vai ser < ou >.
		indiceJato += 1
		indiceJato = indiceJato % len(linha)
		
		if lado == '>': #Empurra pra direita:
			maiorXDaPedra = max(pedraAtual)[0]
			if maiorXDaPedra < 6: # Dá pra mexer pois não grudou na parede da direita ainda.
				daPraDireita = True
				for coordenada in pedraAtual: # verifica para todos os pontos se tem alguma pedra obstruindo a direita.
					coordenadaDireita = (coordenada[0]+1, coordenada[1])
					if coordenadaDireita in mapa: # Alguma delas não dá pra ir pra direita.
						daPraDireita = False
				if daPraDireita:
					for coordenada in pedraAtual:
						coordenada[0] += 1
		else:
			menorXDaPedra = min(pedraAtual)[0]
			if menorXDaPedra > 0: # Dá pra mexer.
				daPraEsquerda = True
				for coordenada in pedraAtual:
					coordenadaEsquerda = (coordenada[0]-1, coordenada[1])
					if coordenadaEsquerda in mapa:
						daPraEsquerda = False
				if daPraEsquerda:
					for coordenada in pedraAtual:
						coordenada[0] -= 1
		daPraDescer = True
		for coordenada in pedraAtual:
			coordenadaInferior = (coordenada[0], coordenada[1] - 1)
			if coordenadaInferior in mapa: # Alguma delas não dá pra descer mais.
				daPraDescer = False
		# Se chegou aqui, é porque todas podem descer + 1.
		if daPraDescer: # Desce 1 em tudo.
			for coordenada in pedraAtual:
				coordenada[1] -= 1
		else: #Acabou.
			maiorY = 0
			for coordenada in pedraAtual:
				maiorY = max(coordenada[1], maiorY)
				mapa[tuple(coordenada)] = None # Adiciona no mapa
				
				
					
				# Ver também se o chão fechou uma linha inteira:
				oChaoFechou=True
				alturaDestaCoordenada = coordenada[1]
				for x in range(7):
					if (x, alturaDestaCoordenada) not in mapa:
						oChaoFechou = False
				if oChaoFechou:
					alturaDoChaoMaisAlto = max(alturaDoChaoMaisAlto, alturaDestaCoordenada)
			menorAlturaSemPedra = max(menorAlturaSemPedra, maiorY + 1)
			
			# Limpar o que tiver abaixo do chão mais alto.
			#if oChaoFechou: #Limpar só se tiver fechado, vai que é muito esforço limpar sempre. 
			#(Não funcionou. Se ficar lento a gente vê depois)
			mapa = {chave: valor for chave, valor in mapa.items() if chave[1]>=alturaDoChaoMaisAlto}
			
			#Agora o menorAlturaSemPedra e o alturaDoChaoMaisAlto estão corretos. 
			# Verificar e salvar no gabarito:
			
			# Gera 7 números, um para cada torre:
			numeros = []
			for indiceColuna in range(7): # para cada torre
				numeroDestaColuna = '' # vai ficar algo do tipo 11010101010.
				for altura in range(alturaDoChaoMaisAlto, menorAlturaSemPedra):
					numeroDestaColuna += '1' if (indiceColuna, altura) in mapa else '0'
				numeros.append(int(numeroDestaColuna, 2))
				
			numeros.append(indiceJato)
			numeros.append(tipoPedra)
			chaveParaSalvarNoGabarito = tuple(numeros)
			if (chaveParaSalvarNoGabarito) in gabarito:
				periodoParaRepetir = indicePedra - gabarito[chaveParaSalvarNoGabarito][0]
				quantoFaltaParaTerminar = objetivoAtual - indicePedra
				#Acho que em teoria precisaria ver se repete antes do primeiro objetivo.
				if periodoParaRepetir != 0:
					quantosPassosPossoPular = quantoFaltaParaTerminar // periodoParaRepetir
					#print('repetiu!', indicePedra, gabarito[chaveParaSalvarNoGabarito])
					indicePedra += (quantosPassosPossoPular * periodoParaRepetir)
					# Precisa atualizar também o mapa todo com N vezes...
					distanciaQueSubiuEm1Periodo = alturaDoChaoMaisAlto - gabarito[chaveParaSalvarNoGabarito][1]
					alturaASubir = quantosPassosPossoPular * distanciaQueSubiuEm1Periodo
					mapa = {(chave[0], chave[1] + alturaASubir) : valor for chave, valor in mapa.items()}
					alturaDoChaoMaisAlto += alturaASubir
					menorAlturaSemPedra += alturaASubir
					
					
			else:
				gabarito[chaveParaSalvarNoGabarito] = (indicePedra, alturaDoChaoMaisAlto)
			
			if (indicePedra == objetivoAtual-1): 
				print('Altura da torre após',objetivoAtual, 'pedras:', menorAlturaSemPedra)
				if (objetivoAtual == objetivoSeguinte): # Acabou
					exit()
				else: #Atualiza o objectivo pra parte 2.
					objetivoAtual = objetivoSeguinte
			break
	indicePedra += 1

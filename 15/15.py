# Desafio do dia 15/12/2022:
# a) Dada uma lista de radares, e o objeto detectado por cada um. Como cada radar só detecta o objeto mais próximo, calcular o número de coordenadas que com certeza não possuem nenhum objeto.
# b) Calcular a única coordenada que não é abrangida por nenhum radar.

with open('input.txt') as file:
	linhas = file.read().splitlines()

def retangularParaDiagonal(x,y): # Função que converte uma coordenada no sistema de eixos retangular para o diagonal (rotacionado de 45 graus).
	novoX = x - y
	novoY = x + y
	return (novoX, novoY)

def diagonalParaRetangular(x,y): # Função inversa.
	novoX = int((x + y) / 2)
	novoY = int((y - x) / 2)
	return (novoX, novoY)

sensores={}
menorX = 10**10
menorY = 10**10
maiorX = 0
maiorY = 0
xBeacons = set() # Coordenadas X dos beacons na linha destino.
linhaDestino = 2000000 # Linha destino para a parte 1.

# Parte 2:
limite = 4000000
xDiagonais = [0]
yDiagonais = [0]

# Adiciona aos intervalos referentes as menores e maiores diagonais em cada eixo:
x, y = retangularParaDiagonal(limite, 0)
xDiagonais.append(x)
yDiagonais.append(y)
x, y = retangularParaDiagonal(0, limite)
xDiagonais.append(x)
yDiagonais.append(y)

for linha in linhas:
	sensor, beacon = linha.split(': ')
	sensor = sensor.split(', ')
	sensor = tuple((map(lambda x: int(x.split('=')[1]), sensor)))
	beacon = beacon.split(', ')
	beacon = tuple((map(lambda x: int(x.split('=')[1]), beacon)))	
	if beacon[1] == linhaDestino:
		xBeacons.add(beacon[0])
	distanciaMaxima = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
	sensores[sensor] = distanciaMaxima
	menorX = min(menorX, sensor[0]-distanciaMaxima)
	maiorX = max(maiorX, sensor[0]+distanciaMaxima)
	menorY = min(menorY, sensor[1]-distanciaMaxima)
	maiorY = max(maiorY, sensor[1]+distanciaMaxima)
	
	# Parte 2:
	x, y = sensor
	coordenadaEsquerda = (x - distanciaMaxima, y) #
	coordenadaDireita = (x + distanciaMaxima, y)
	xDiagonal1, yDiagonal1 = retangularParaDiagonal(*coordenadaEsquerda)
	xDiagonal2, yDiagonal2 = retangularParaDiagonal(*coordenadaDireita)
	xDiagonais.append(xDiagonal1)
	xDiagonais.append(xDiagonal2)
	yDiagonais.append(yDiagonal1)
	yDiagonais.append(yDiagonal2)
	intervaloX = tuple(sorted((xDiagonal1, xDiagonal2)))
	intervaloY = tuple(sorted((yDiagonal1, yDiagonal2)))

resposta = 0
for idx in range(menorX, maiorX+1):
		coordenada = (idx, linhaDestino)
		for sensor, distanciaMax in sensores.items():
			if coordenada[0] in xBeacons: continue
			distancia = abs(coordenada[0] - sensor[0]) + abs(coordenada[1] - sensor[1])
			if distancia <= distanciaMax:
				resposta+=1
				break
print('A quantidade de coordenadas que não podem ser beacon na linha é:', resposta)

# Parte 2:
yDiagonais = list(set(yDiagonais))
xDiagonais = list(set(xDiagonais))
yDiagonais.sort()
xDiagonais.sort()
for xDiagonal in xDiagonais:
	for yDiagonal in yDiagonais:
		# Algum desses precisa ser o imediatamente anterior a resposta correta:
		xCandidato = xDiagonal + 1
		yCandidato = yDiagonal + 1
		xCandidato, yCandidato = diagonalParaRetangular(xCandidato, yCandidato)
		respostaCandidata = (xCandidato, yCandidato)
		if xCandidato > limite or xCandidato < 0: continue
		if yCandidato > limite or yCandidato < 0: continue
		estaNoAlcanceDeAlgumSensor = False
		for sensor, distanciaMaxima in sensores.items(): # Para cada sensor:
			# Caso a distancia dessa coordenada para o sensor seja menor ou igual a distancia máxima:
			distancia = abs(sensor[0] - xCandidato) + abs(sensor[1]- yCandidato)
			if distancia <= distanciaMaxima: # Esse ponto está dentro do alcance desse sensor.
				estaNoAlcanceDeAlgumSensor = True # Logo não é uma coordenada válida para a resposta.
		if not estaNoAlcanceDeAlgumSensor:
			frequencia = respostaCandidata[0] * 4000000 + respostaCandidata[1]
			print('A frequência da única posição possível para o beacon é:', frequencia)

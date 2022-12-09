# Desafio do dia 09/12/2022:
# a) Receber uma lista de instruções que o começo de uma corda vai seguir. Calcular em quantas posições a cauda passou.
# b) Idem, porém para uma corda de tamanho 9.

with open('input.txt') as file:
	instrucoes = file.read().splitlines()

posicoesVisitadasPelaCauda = {(0,0)} # Resposta para a parte 1.
posicoesVisitadasPelaCauda9 = {(0,0)} # Idem para a parte 2.
cauda = (0,0)
cabeca = (0,0)
nos = [(0,0) for _ in range(10)] # A parte 1 poderia ser feita na parte 2, olhando os nós 2 e 9 da corda.

def estaoTocando(coordenada1, coordenada2):
	for idx in range(-1, 2):
		for idy in range(-1, 2):
			if (coordenada1[0] + idx, coordenada1[1] + idy) == coordenada2:
				return True
	return False

for instrucao in instrucoes:
	direcao, quantidade = instrucao.split()
	quantidade = int(quantidade)

	if direcao == 'R':
		delta = (1, 0)
	elif direcao == 'L':
		delta = (-1, 0)
	elif direcao == 'U':
		delta = (0, 1)
	elif direcao == 'D':
		delta = (0, -1)

	for _ in range(quantidade):
		cabeca = (cabeca[0] + delta[0], cabeca[1] + delta[1]) # Move a cabeça.
		if not estaoTocando(cauda, cabeca):
			distancia = (cabeca[0] - cauda[0], cabeca[1] - cauda[1])
			distancia = [x / abs(x) if x != 0 else 0 for x in distancia] # Pode-se mover 1 em cada eixo.
			cauda = (cauda[0] + distancia[0], cauda[1] + distancia[1])
			posicoesVisitadasPelaCauda.add(cauda)

	# Parte 2:
		nos[0] = (nos[0][0] + delta[0], nos[0][1] + delta[1]) # Move a cabeça.
		for indiceNo in range(9): # Cada nó se baseia no nó anterior.
			noPai = nos[indiceNo] # Nó que está puxando.
			noFilho = nos[indiceNo + 1] # Nó que está sendo puxado.
			if not estaoTocando(noPai, noFilho):
				distancia = (noPai[0] - noFilho[0], noPai[1] - noFilho[1])
				distancia = [x / abs(x) if x != 0 else 0 for x in distancia]
				# Move o nó filho:
				nos[indiceNo + 1] = (nos[indiceNo + 1][0] + distancia[0],
									 nos[indiceNo + 1][1] + distancia[1])
		posicoesVisitadasPelaCauda9.add(nos[9])
		# PosicoesParte1.add(nos[1]) traria a resposta da parte 1 sem repetição de código.

print('Para uma corda de tamanho 2, o número de posições que a cauda visitou é:', len(posicoesVisitadasPelaCauda))
print('Para uma corda de tamanho 9, o número de posições que a cauda visitou é:', len(posicoesVisitadasPelaCauda9))

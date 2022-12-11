# Desafio do dia 11/12/2022:
# a) Receber uma lista de instruções em que cada nó possui instruções de divisão e remanejamento das informações.
# b) Idem porém para uma quantidade maior de turnos e sem dividir por três a cada etapa. 

with open('input.txt') as file:
	linhas = file.read()
	linhasMacacos = linhas.split('\n\n')

macacos = {} # Dicionário que contém as informações de cada macaco.
macacos2 = {} # Cópia para parte 2. 
informacoesMacacos = {} # Dicionário que relaciona cada macaco a seus dados (divisores, testes, etc).
divisorGlobal = 1 # É o MMC entre os divisores de todos os macacos.
for linhasMacaco in linhasMacacos:
	linhas = linhasMacaco.splitlines()
	numero = int(linhas[0].split(' ')[1][-2]) # Caso algum macaco tenha seu número fora de ordem.
	itens = linhas[1].split(': ')[1].split(', ')
	itens = list(map(int, itens))
	operacao = linhas[2].split('= ')[1]
	divisorTeste = int(linhas[3].split()[-1]) # Presume que todos os testes são de divisão.
	divisorGlobal *= divisorTeste
	destinoVerdadeiro = int(linhas[4].split()[-1])
	destinoFalso = int(linhas[5].split()[-1])
	informacoes = (operacao, divisorTeste, destinoVerdadeiro, destinoFalso)
	informacoesMacacos[numero] = informacoes
	macacos[numero] = itens
	macacos2[numero] = itens.copy()

numeroDeInspecoes = {numero: 0 for numero in macacos}
numeroDeInspecoes2 = {numero: 0 for numero in macacos2}

for indiceRound in range(10000):
	indicesMacacos = list(macacos.keys())
	indicesMacacos.sort()
	for indice in indicesMacacos: # Para cada macaco:
		itens = macacos[indice]
		operacao, divisorTeste, destinoVerdadeiro, destinoFalso = informacoesMacacos[indice]
		for _ in range(len(itens)): # Para cada item que ele segura atualmente:
			if indiceRound>20: break
			item = itens.pop(0)
			valorPosOperacao = eval(operacao.replace('old', str(item)))
			valorPosArredondamento = int(valorPosOperacao / 3)
			destino = destinoVerdadeiro if valorPosArredondamento % divisorTeste == 0 else destinoFalso
			macacos[destino].append(valorPosArredondamento)
			numeroDeInspecoes[indice] += 1
		# Parte 2:
		itens = macacos2[indice]
		for _ in range(len(itens)): # Para cada item que ele segura atualmente:
			item = itens.pop(0)
			valorPosOperacao = eval(operacao.replace('old', str(item)))
			destino = destinoVerdadeiro if valorPosOperacao % divisorTeste == 0 else destinoFalso
			macacos2[destino].append(valorPosOperacao % divisorGlobal)
			numeroDeInspecoes2[indice] += 1

	if indiceRound +1 == 20: # Imprime a resposta da primeira parte.
		inspecoes = [quantidade for quantidade in numeroDeInspecoes.values()]
		inspecoes.sort(reverse = True)
		print('Valor após 20 rounds:', inspecoes[0] * inspecoes[1])

inspecoes = [quantidade for quantidade in numeroDeInspecoes2.values()]
inspecoes.sort(reverse = True)
print('Valor após 10000 rounds:', inspecoes[0] * inspecoes[1])

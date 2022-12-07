# Desafio do dia 07/12/2022:
# a) Receber uma lista de comandos do terminal (cd e ls) que montam uma árvore de arquivos. Calcular qual o maior diretório existente.
# b) Calcular qual o menor diretório existente para liberar uma certa quantidade de espaço.

with open('input.txt') as file:
	comandos = file.read().splitlines()

diretorios = {} # Dicionário multi-nível que contém toda a árvore de arquivos.
diretoriosPais = {} # Dicionario que relaciona o id de cada diretório a seu diretório pai.
diretorioAtual = diretorios

for comando in comandos:
	palavras = comando.split()
	if palavras[0] == '$': # É um comando.
		if palavras[1] == 'ls':
			pass	# Como a listagem de arquivos e diretórios é bem definida, não há necessidade de fazer algo.
		elif palavras[1] == 'cd': # Mudança de diretório.
			if palavras[2] == '..': # Subir um nível.
				diretorioAtual = diretoriosPais[id(diretorioAtual)]
			else:
				destino = palavras[2]
				if destino not in diretorioAtual: # Prevenção caso seja usado 'cd' antes de 'ls'.
					subdiretorio = {}
					diretorioAtual[destino] = subdiretorio
					diretoriosPais[id(subdiretorio)] = diretorioAtual
				diretorioAtual = diretorioAtual[destino]				

	elif palavras[0] == 'dir': # É uma das subpastas sendo listadas.
		nomeDiretorio = palavras[1]
		subdiretorio = {}
		if nomeDiretorio not in diretorioAtual: # Prevenção caso seja usado 'cd' antes de 'ls'.
			diretorioAtual[nomeDiretorio] = subdiretorio # No meu input essa prevenção não foi necessária.
		diretoriosPais[id(subdiretorio)] = diretorioAtual

	else: # É um dos arquivos sendo listados.
		tamanho, nomeArquivo = int(palavras[0]), palavras[1]
		diretorioAtual[nomeArquivo] = tamanho

tamanhosDiretorios = {} # Dicionário que relaciona o id de cada diretório a seu tamanho.
def verificarTamanho(diretorio): # Função que popula recursivamente o dicionário de tamanhos.
	tamanhoDesteDiretorio = 0
	for valor in diretorio.values():
		if type(valor) is int: # É um arquivo.
			tamanhoDesteDiretorio += valor
		else: # É um subdiretorio.
			tamanhoDesteDiretorio += verificarTamanho(valor) # Calcula o tamanho do diretório interno.
	tamanhosDiretorios[id(diretorio)] = tamanhoDesteDiretorio # Salva o tamanho.
	return tamanhoDesteDiretorio

verificarTamanho(diretorios['/']) # Chama a função no diretório raiz para calcular os tamanhos.
resposta = 0
for tamanho in tamanhosDiretorios.values():
	if tamanho < 100000: # Apenas os diretórios menores que um certo tamanho são considerados.
		resposta += tamanho
print('A soma dos tamanhos menores que 100000 é:', resposta)

# Parte 2:
espacoTotal = 70000000
espacoUsado = tamanhosDiretorios[id(diretorios['/'])]
espacoLivre = espacoTotal - espacoUsado
espacoQueFalta = 30000000 - espacoLivre
tamanhos = [tamanho for tamanho in tamanhosDiretorios.values() if tamanho >= espacoQueFalta]
tamanhos.sort()
print('O tamanho do menor diretório que libera espaço suficiente é:', tamanhos[0])

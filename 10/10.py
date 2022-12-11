# Desafio do dia 10/12/2022:
# a) Receber uma lista de instruções em um processador com apenas um registrador e calcular o valor após determinadas quantidades de ciclos.
# b) Usar os valores do registrador para desenhar uma matriz de pixels e verificar o que está escrito em tela.
with open('input.txt') as file:
	instrucoes = file.read().splitlines()

numeroDeCiclos = 0
registrador = 1
soma = 0
tela = ''

def incrementarQuantidadeDeCiclos(quantidade):
	global soma, numeroDeCiclos, tela, registrador
	for _ in range(quantidade):
		if numeroDeCiclos % 40 in range(registrador - 1, registrador + 2): # Parte 2:
			tela += '#'
		else: 
			tela += ' '

		numeroDeCiclos += 1
		if numeroDeCiclos % 40 == 20:
			soma += (registrador * numeroDeCiclos)
		if numeroDeCiclos % 40 == 0: # Adiciona uma quebra de linha para facilitar a leitura da parte 2.
			tela += '\n'

for instrucao in instrucoes:
	palavras = instrucao.split()
	incrementarQuantidadeDeCiclos(1)
	if len(palavras) == 2: # Caso tenha valor, significa que é a operação de adição:
		valor = int(palavras[1])
		incrementarQuantidadeDeCiclos(1)
		registrador += valor

print('A soma da força dos seis sinais é:', soma)
print(tela)

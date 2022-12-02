# Desafio do dia 02/12/2022:
#a) Receber uma lista de jogadas de pedra, papel e tesoura e calcular a pontuação total.
#b) Idem, porém ao invés de receber as duas escolhas, você recebe uma escolha e o resultado da partida.

with open ("input.txt") as file:
	partidas = file.read().splitlines()

resposta = 0
respostaParte2 = 0
for partida in partidas:
	a, b = partida.split()
	if a == 'A':
		if b == 'X':
			pontuacao = 1 + 3
			pontuacaoParte2 = 3 + 0
		elif b == 'Y':
			pontuacao = 2 + 6
			pontuacaoParte2 = 1+3
		elif b == 'Z':
			pontuacao = 3 + 0
			pontuacaoParte2 = 2 + 6

	elif a == 'B':
		if b == 'X':
			pontuacao = 1 + 0
			pontuacaoParte2 = 1 + 0
		elif b == 'Y':
			pontuacao = 2 + 3
			pontuacaoParte2 = 2 + 3
		elif b == 'Z':
			pontuacao = 3 + 6
			pontuacaoParte2 = 3 + 6

	elif a == 'C':
		if b == 'X':
			pontuacao = 1 + 6
			pontuacaoParte2 = 2 + 0
		elif b == 'Y':
			pontuacao = 2 + 0
			pontuacaoParte2 = 3 + 3
		elif b == 'Z':
			pontuacao = 3 + 3
			pontuacaoParte2 = 1 + 6

	resposta += pontuacao
	respostaParte2 += pontuacaoParte2

print('Pontuação utilizando a primeira interpretação:', resposta)
print('Pontuação utilizando a segunda interpretação:', respostaParte2)

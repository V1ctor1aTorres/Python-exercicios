jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range (0, tot):
    partidas.append(int(input(f'Quantos gol nas partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')


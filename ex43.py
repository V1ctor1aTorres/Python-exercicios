from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opçoes:
[0] Pedra
[1] Papel
[2] Tesoura''')
jog = int(input('Qual sua jogada? '))
print('-=' * 10)
if pc == 0:
    if jog == 0:
        print('Empate!')
    elif jog == 1:
        print('Jogador ganhou!')
    elif jog ==2:
        print('Maquina ganhou!')
    else:
        print('Invalido!')
elif pc == 1:
    if jog == 0:
        print('Jogador ganhou!')
    elif jog == 1:
        print('Empate!')
    elif jog ==2:
        print('Maquina ganhou!')
    else:
        print('Invalido!')
elif pc == 2:
    if jog == 0:
        print('Jogador ganhou!')
    elif jog == 1:
        print('Maquina ganhou!')
    elif jog ==2:
        print('Empate!')
    else:
        print('Invalido!')



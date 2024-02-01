from random import randint
computador = randint(0, 5)
jogador = int(input('Em que numero eu pensei? '))

if computador == jogador:
    print('Parabens, vc adivinhou!')
else:
    print('Você errou!')
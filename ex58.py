from random import randint
pc = randint(0,5)
print('Sou seu computador! Acabei de pensar num numero entre 0 e 10.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais...')
        else:
            print('Menos...')
print('Acertou com {} palpites!'.format(palpites))
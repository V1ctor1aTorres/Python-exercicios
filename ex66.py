from random import randint
v = 0
while True:
    jogador = int(input('Digite um numero'))
    computador = int(input(0, 11))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
        break
    elif tipo == "I":
        if total % 2 == 1:
            print('Voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break




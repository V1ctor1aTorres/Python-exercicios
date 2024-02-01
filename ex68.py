total = totmil = menor = cont = 0
while True:
    n = str(input('Qual o nome do produto? '))
    p = float(input('Qual o preço do produto? '))
    cont += 1
    total += p
    if p > 1000:
        totmil += 1
    if cont == 1:
        menor = p
    else:
        if p < menor:
            menor = p
    c = ' '
    while c not in 'SN':
        c = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        break
print(f'O total da compra foi {total}')
print(f'Temos {totmil} produtos de mais 1000')
print(f'O produto mais barato custa R${menor}')
print('Fim')


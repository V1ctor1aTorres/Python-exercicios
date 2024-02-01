temp = []
prin = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(prin) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Os dados foram {prin}')
print(f'Ao todo voce cadastrou {len(prin)} pessoas')
print(f'O maior peso foi de {mai} quilos')
print(f'O menor peso foi de {men} quilos')



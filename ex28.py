dis = float(input('Qual a distancia da viagem em KMs?'))
c = dis * 0.50
l = dis * 0.45

if dis <= 200:
    print('A viagem custa R${:.2f}'.format(c))
else:
    print('A viagem custa R${:.2f}'.format(l))

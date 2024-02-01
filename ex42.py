peso = float(input('Peso: '))
alt = float(input('altura: '))
imc = peso / (alt ** 2)
print('O imc é {:.1f}'.format(imc))

if imc < 18.5:
    print('abaixo do peso:')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30<= imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')


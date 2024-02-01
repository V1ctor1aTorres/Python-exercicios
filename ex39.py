n1 = float(input('digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('reprovado')
elif media == 5 or media <= 6.9:
    print('recuperaçao')
else:
    print('Aprovado')

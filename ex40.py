from datetime import date
ano = date.today().year
a = int(input('Digite seu ano de nascimento:'))
idade = ano - a

print('Quem nasceu em {} tem {} anos.'.format(a, idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')

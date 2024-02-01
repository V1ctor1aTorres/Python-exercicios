from datetime import date
atual = date.today().year
ano = int(input('digite o ano de nascimento: '))
idade = atual - ano
f = 18 - idade
p = idade - 18
if idade < 18:
    print('ainda vai se alistar, faltam {} anos.'.format(f))
elif idade == 18:
    print('Hora de alistar')
else:
    print('O alistamento ja passou ha {} anos pra você'.format(p))

n = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo é: {}.'.format(n))
nomes = n.split()
print('Seu primeiro nome é: {}'.format(nomes[0]))
print('Seu ultimo nome é: {}.'.format(nomes[len(nomes)-1]))


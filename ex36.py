num = int(input('Digite um numero: '))
print('''Escolha uma das bases de conversão:
[1] binário
[2] otogonal
[3] hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido pra binario é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octogonal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida tente novamente!')




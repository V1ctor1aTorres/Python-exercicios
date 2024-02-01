from time import sleep
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print('Os numeros escolhidos foram: {} e {}'.format(n1, n2))
opcao = 0
while opcao != 5:
    print('=-' * 20)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do Programa''')
    print('=-' * 20)
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior'.format(n1))
        else:
            print('{} é maior'.format(n2))
    elif opcao == 4:
        print('Informe os numeros novamente.')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente Novamente.')
        sleep(2)
print('------Fim------')


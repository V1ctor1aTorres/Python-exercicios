print('Gerador de PA')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos numeros voce quer mostrar a mais?'))
print('FIM!')
print('Progressao finalizada com {} termos mostrados!'.format(total))



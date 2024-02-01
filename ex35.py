valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario do comprador? '))
anos = int(input('Em quantos anos vai pagar a casa?'))
prestação = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos , a prestação será de R${:.2f} mensais.'.format(valor, anos, prestação))
if prestação <= minimo:
    print('Emprestimo concedido')
else:
    print('Emprestimo negado!')




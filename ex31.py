sal = float(input('Qual o salario? '))
if sal <= 1250:
    a = (sal * 15 / 100) + sal
    print('O novo salario é: R${}'.format(a))
else:
    a = (sal * 10 / 100) + sal
    print('O novo salario é R${}'.format(a))


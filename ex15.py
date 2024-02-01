import random
n1 = str(input('Digite um nome de aluno: '))
n2 = str(input('Digite outro nome de aluno: '))
n3 = str(input('Digite outro nome de aluno: '))
n4 = str(input('Digite outro nome de aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
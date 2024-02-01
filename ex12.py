import math
num = float(input('Digite um numero: '))
print('o numero digitado é {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))


from math import trunc
num = float(input('Digite um numero: '))
print('o numero digitado é {} e a sua porção inteira é {}.'.format(num, trunc(num)))


num = float(input('Digite um numero: '))
print('o numero digitado é {} e a sua porção inteira é {}.'.format(num, int(num)))
f = str(input('Digite uma frase')).upper().strip()
print('A frase tem {} letras A.'.format(f.count('A')))
print('A primeira letra A aparece na posição {}.'.format(f.find('A')+1))
print('A ultima letra A aparece na posição {}.'.format(f.rfind('A')+1))

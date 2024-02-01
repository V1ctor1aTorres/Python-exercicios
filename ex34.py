nome = str(input('qual seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Maria' or nome == 'Paulo':
    print('Nome popular no brasil')
else:
    print("Seu nome é bem normal")
print('Tenha um bom dia {}.'.format(nome))


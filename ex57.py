sexo = str(input('Informe seu sexo: [S/M]')).strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos! Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

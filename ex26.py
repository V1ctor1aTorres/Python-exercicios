vel = float(input('qual a velocidade do carro?'))
mu = int((vel - 80) * 7)

if vel > 80:
    print('Você foi multado em {} R$.'.format(mu))
print('Sua velocidade foi {} Km. Tenha um bom dia!'.format(vel))

def voto():
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} voto opcional!'
    else:
        return f'Voto OBRIGATÓRIO!!!!'


nasc = int(input("Qual seu ano de nascimento?"))
print(voto(nasc))




def voto(n):
    from datetime import date
    idade = date.today().year - n
    if idade > 65 or 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO!'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
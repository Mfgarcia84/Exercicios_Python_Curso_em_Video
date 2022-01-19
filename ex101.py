'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal (frase/palavra) indicando se uma pessoa tem voto NEGADO, OPCIONAL, ou
OBRIGATÓRIO nas eleições.
'''


def voto(ano):
    from datetime import date #import apenas dentro da função economiza memória
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} ano: NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


ano = int(input('Em que ano você nasceu? '))
voto(ano)

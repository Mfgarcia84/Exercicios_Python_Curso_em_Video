'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o 
total de vitórias consecutivas que ele consquistou no final do jogo.'''

#minha solução = solução da aula
from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
c = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    par_ou_impar = ' '
    soma = jogador + computador
    while par_ou_impar not in 'PI':
        par_ou_impar = str(input('Par ou Ímpar? [P/I] ')).replace(' ','').upper()[0]
    if soma % 2 == 0: #par
        if par_ou_impar == 'P':
            print('jogador ganhou!')
        else:
            print('computador ganhou!')
            break
    else: #impar
        if par_ou_impar == 'I':
            print('jogador ganhou!')
        else:
            print('computador ganhou!')
            break
    c = c + 1
print('~'*45)
print(f'Você jogou {jogador} e o computador jogou {computador}.')
print('O resultado deu PAR' if soma % 2 == 0 else 'O resultado deu IMPAR!')
print(f'Você teve {c} vitórias consecutivas.')
print('~'*45)
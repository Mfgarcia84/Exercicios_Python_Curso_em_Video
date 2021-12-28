'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, 
na ordem de colocação. Depois mostre: 
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da chapecoense'''

colocados = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 
        'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 
        'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
        'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 
        'Chapecoense')

indice_chapecoense = colocados.index('Chapecoense') + 1

print('-='*70)
#a) apenas os 5 primeiros colocados
print(f'Os cinco primeiros colocados são: {colocados[0:5]}')
print('-='*70)
#b) os últimos 4 colocados da tabela
print(f'Os últimos quatro colocados são: {colocados[-4:]}')
print('-='*70)
#c) uma lista com os times em ordem alfabética
print(f'Times em ordem alfabética é: {sorted(colocados)}')
print('-='*70)
#d) em que posição na tabela está o time da chapecoense
print(f'A Chapecoense encontra-se na {indice_chapecoense}ª posição.')
print('-='*70)
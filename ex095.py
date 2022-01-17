'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador.
'''

time = []
jogador = {}
gols = []
print('==' * 20)
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols'] = gols[:]
    time.append(jogador.copy())
    gols.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resposta == 'N':
        break
    print('==' * 20)
print(jogador)
print(time)


print('-='*30)
print(f'{"cod"} {"nome":<10} {"gols":<10} {"total":<10}')
print('-='*30)
for c in range(len(time)):
    print(f'{c} {time[c]["nome"]} {time[c]["gols"]} {sum(time[c]["gols"])}')
print('-='*30)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if mostrar == 999:
        break
    elif mostrar >= len(time):
        print(f'Erro! Não existe jogador com o código {mostrar}')
    else:
        for c in range(len(time)):
            if mostrar == c:
                print(f'--LEVANTAMENTO DO JOGADOR {time[c]["nome"]}:')
                for j, g in enumerate(time[c]['gols']):
                    print(f'No jogo {j} fez {g} gols.')




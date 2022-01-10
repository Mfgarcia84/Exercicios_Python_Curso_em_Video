'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo total de gols feitos durante o campeonato.
'''

jogador = {}
gols = []
jogador['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['gols'] = gols[:] #não esquecer da fazer uma cópia
jogador['total'] = sum(gols) #gols é uma lista, logo podemos fazer a soma dos elementos
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas:')
for i in range(partidas):
    print(f'Na partida {i+1}, fez {jogador["gols"][i]} gols.')

'''outra opção para o último for
for k,v in enumerate(jogador['gols']):
    print(f'Na partida {k}, fez {v} gols.')'''



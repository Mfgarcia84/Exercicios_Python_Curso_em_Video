'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo total de gols feitos durante o campeonato.
'''
tot = 0
dados = {}
gols = []
dados['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    tot = tot + gols[i]
dados['gols'] = gols
dados['total'] = tot
print('-='*20)
print(dados)
print('-='*20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas:')
for i in range(partidas):
    print(f'Na partida {i+1}, fez {dados["gols"][i]} gols.')




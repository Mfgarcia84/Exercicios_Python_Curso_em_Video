'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados num dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número do dado.
'''
import  operator
jogadas = dict()
from random import randint
from time import sleep
print('Valores sorteados:')
jogadas['jogador1'] = randint(1,6)
jogadas['jogador2'] = randint(1,6)
jogadas['jogador3'] = randint(1,6)
jogadas['jogador4'] = randint(1,6)
for k, v in jogadas.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-='*11)
print('Ranking dos jogadores:')
ranking = sorted(jogadas, key=jogadas.get, reverse=True)
c = 1
for i in ranking:
    print(f'{c}° Lugar: {i} com {jogadas[i]}')
    c = c + 1


''' outra opção para outra parte do código
jogadasordenada = sorted(jogadas.items(),key=operator.itemgetter(1), reverse=True)
for i in range(len(jogadasordenada)):
    print(f'{i+1}° Lugar: {jogadasordenada[i][0]} com {jogadasordenada[i][1]}')
    
    
O jogadas.items devolve o par de elementos do dicionário de valor chave
key=operator.itemgetter(1) especifica que a chave de comparação é o valor do dicionário
operator.itemgetter(0) tem a chave de comparação da chave do dicionário.
'''
'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e
somapar(). A primeira função vai sortear 5 números e vai colocá-la dentro da lista e a
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep


def sorteio(lista): #sorteia cinco números e insere na lista
    print('Sorteando 5 valores da lista: ', end='')
    for jogada in range(5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num}', end=' ')
        sleep(0.4)
    print('PRONTO!')

def somapar(lista): #mostra a soma entre os valores pares da função anterior
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma = soma + i
    print(f'Somando os valores pares de {lista}, temos: {soma}', end='')



#programa principal
numeros = []
sorteio(numeros)
somapar(numeros)
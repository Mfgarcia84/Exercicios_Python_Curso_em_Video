'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é maior.
'''

from time import sleep
def maior(*n):
    print('-=' * 25)
    print('Analisando os valores passados...')
    for i in n:
        print(i, end=' ')
        sleep(0.5)
    print(f'\nForam informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {max(n)}.')

maior(11,3,43,65,12,9,7)
maior(7,4,6,8)
maior(1,2)
maior(0)
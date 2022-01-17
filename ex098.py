'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo
e realize a seguinte contagem. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada (usuário digita o início, fim e o passo)
'''

from time import sleep

def contador(inicio, fim, passo=1):
        print('-=' * 15)
        print(f'Contagem de {inicio} até {fim} de {passo if passo>= 0 else -1*passo} em {passo if passo>= 0 else -1*passo}:')
        if inicio < fim:
            for i in range(inicio, fim+1, passo):
                print(i, end=' ')
                sleep(0.5)
            print('FIM!')
        elif inicio > fim:
            for i in range(inicio, fim-1, -1*passo if passo >= 0 else passo):
                print(i, end=' ')
                sleep(0.5)
            print('FIM!')


contador(1,10,1)
contador(10,1,2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
contador(inicio, fim, passo)

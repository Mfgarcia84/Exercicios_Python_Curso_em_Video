'''Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros
elementos de uma sequência de Fibonacci
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''

termos = int(input('Informe a quantidade de termos: '))
c = 3
t1 = 0
t2 = 1
print('{} --> {} --> '.format(t1, t2),end='')
while c <= termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c = c + 1
    print('{} --> '.format(t3),end='')
print('FIM')
'''Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros
elementos de uma sequência de Fibonacci
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''

qtd_termos = int(input('Digite a quantidade de termos da sequência: '))
n=1
while n <= qtd_termos:
    print('0'
    n = n + 1

# n>= 1
# f1 e f2 = 1
# f(n+2) = f(n+1) + f(n)
#
# para n=1
# f3 = f2 + f1 = 1 + 1 = 2
#
# para n=2
# f4 = f3 + f2 = 2 + 1 = 3
#
# para n=3
# f5 = f4 + f3 = 3 + 2 = 5
#
# para n=4
# f6 = f5 + f4 = 5 + 3 = 8
'''Faça um programa que leia um número qualquer e mostre seu fatorial
ex: 5!=5x4x3x2x1=120'''

#minha solução
from math import factorial
num = int(input('Digite um número: '))
print('O fatorial de {} é:'.format(num))
c = num
while c > 0:
    print(c, 'x' if c > 1 else '=', sep=' ', end=' ')
    c = c - 1
print(factorial(num))

#solução aula
'''num = int(input('Digite um número: '))
print('O fatorial de {}! é:'.format(num))
c = num
f = 1
while c > 0:
    print(c, 'x' if c > 1 else '=', sep=' ', end=' ')
    f = c * f
    c = c - 1
print(f)'''

#solução com FOR
'''num = int(input('Digite um número: '))
f = 1
print('O fatorial de {}! é:'.format(num))
for c in range (num, 0, -1):
    print(c, 'x' if c > 1 else '=', end=' ')
    f = f * c
print(f)'''




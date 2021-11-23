'''Faça um programa que leia um número qualquer e mostre seu fatorial
ex: 5!=5x4x3x2x1=120'''
import math
num = int(input('Digite um número: '))
c = num
while c > 0: # solução com WHILE
    print('{}'.format(c),end='')
    print('x' if c > 1 else '=',end='')
    c = c -1
f = math.factorial(num)
print(f)


# num = int(input('Digite um número: ')) # solução com FOR
# c = num
# f = 1
# for c in range(num,0,-1):
#     print(c,end='')
#     print('x' if c > 1 else '=',end='')
#     f = f * c
# print(f)


# num = int(input('Digite um número: '))
# c = num
# while c > 0:
#     print('{}'.format(c),end='')
#     print('x' if c > 1 else '=',end='')
#     if c > 1:
#         f = num * (c-1)
#         num = f
#     c = c - 1
# print(f)


# num = int(input('Digite um número para calcular seu fatorial: '))
# c = num
# f = 1
# while c > 0:
#     print('{}'.format(c),end='')
#     print('x' if c > 1 else '=',end='')
#     f = f * c
#     c = c - 1
# print(f)






# cont = num - 1
# while cont > 0:
#     fatorial = num * cont
#     num = fatorial
#     cont = cont - 1
# print('O fatorial de {} é {}.'.format(num,fatorial))
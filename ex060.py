'''Faça um programa que leia um número qualquer e mostre seu fatorial
ex: 5!=5x4x3x2x1=120'''
num = int(input('Digite um número para calcular seu fatorial: '))
c = 1
while c <= num:
    x = num * (num-c)
    print(x)
    c = c + 1
    num = x






# cont = num - 1
# while cont > 0:
#     fatorial = num * cont
#     num = fatorial
#     cont = cont - 1
# print('O fatorial de {} é {}.'.format(num,fatorial))
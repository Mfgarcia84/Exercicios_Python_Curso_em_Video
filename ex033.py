#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
# print('O maior número é {}.'.format(max(n1,n2,n3))) outra maneira com função
# print('O menor número é {}.'.format(min(n1,n2,n3))) outra maneira com função

if n1<n2 and n1<n3:
    print('{} é menor.'.format(n1))
if n2<n1 and n2<n3:
    print('{} é menor.'.format(n2))
if n3<n1 and n3<n2:
    print('{} é menor.'.format(n3))
if n1>n2 and n1>n3:
    print('{} é maior.'.format(n1))
if n2>n1 and n2>n3:
    print('{} é maior.'.format(n2))
if n3>n1 and n3>n2:
    print('{} é maior.'.format(n3))






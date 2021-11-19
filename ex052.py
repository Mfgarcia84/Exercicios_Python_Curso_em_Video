#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

t = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0 and num % num == 0:
        print('\033[31m',c,'\033[m',end=' ')
        t = t + 1
    else:
        print(c,end=' ')
if t == 2:
    print('\nO número {} é divisível por {} números e é primo.'.format(num,t))
else:
    print('\nO número {} é divisível por {} número(s) e não é primo.'.format(num,t))


# t = 0
# num = int(input('Digite um número: '))
# for c in range(1, num+1):
#     if num % c == 0:
#         print('\033[31m',c,'\033[m',end='')
#         t = t + 1
#     else:
#         print(c,end=' ')
# if t == 2:
#     print('\nO número é PRIMO.')
# else:
#     print('\nO número NÃO É PRIMO.')


# num = int(input('Digite um número: '))
# s = 0
# for c in range(1, num+1):
#     if num % c == 0: #quais os valores de 'c' que atenderam essa condição?
#         print('\033[32m{}\033[m'.format(c),end=' ') #mostre quais valores de 'c' atenderam a condição if e pinte de verde
#         s = s + 1
#     else:
#         print('\033[31m{}\033[m'.format(c),end=' ') #mostre quais valores de 'c' não atenderam a condição if e pinte de vermelho
# print('\nO número {} é divisível {} vezes.'.format(num, s))
# if s == 2:
#     print('\nO número É PRIMO!')
# else:
#     print('\nO número NÃO É PRIMO!')


#mesmo programa mas um pouco diferente
# num = int(input('Digite um número: '))
# tot = 0
# for c in range(1, num+1):
#     if num % c == 0:
#         print('\033[31m{}\033[m'.format(c),end=' ')
#         tot = tot + 1 # tot + =1
#     else:
#         print('{}'.format(c),end=' ')
# print('\nO número {} foi divisível {} vezes.'.format(num,tot))
# if tot == 2:
#     print('O número É PRIMO!')
# else:
#     print('O número NÃO É PRIMO!')



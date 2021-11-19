#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

print()
print('-='*20)
print(' '*10,'DESAFIO 005')
print('-='*20)
num = int(input('Digite um número: '))
suc = num + 1
ant = num - 1
# #print('O sucessor de {} é {} e o antecessor de {} é {}.'.format(num,suc,num,ant))
#
print('O sucessor de {}{}{} é {}{}{} e o antecessor é {}{}{}.'.format('\033[32m',num,'\033[m','\033[31m',(num+1),'\033[m','\033[1:30:46m',(num-1),'\033[m'))

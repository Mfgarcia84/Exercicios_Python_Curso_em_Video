#crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
resto = num % 2
#print(resto)
if resto == 0:
    print('O número é \033[1:30:46mpar.\033[m')
else:
    print('O número é \033[1:30:41mímpar.\033[m')

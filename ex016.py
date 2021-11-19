#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
print()
print('='*25,'DESAFIO 016','='*25)
num = float(input('Digite um número: '))
print('O número {} tem sua parte inteira {}.'.format(num,math.floor(num)))#floor reduz a casa decimal para zero até o menor número inteiro

#ou
# import math
# num = float(input('Digite um número: '))
# print('{}'.format(math.trunc(num))) trunc vai cortar a parte inteira do número

#ou
# num = float(input('Digite um valor: '))
# print('{}'.format(int(num))) sem importar módulos

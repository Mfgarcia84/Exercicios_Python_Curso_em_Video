#Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#a^2=b^2+c^2
import math
print()
print('='*25,'DESAFIO 017','='*25)
b = float(input('Digite o valor do cateto oposto: '))
c = float(input('Digite o valor do cateto adjacente: '))
a = math.sqrt(b**2+c**2)
print('A hipotenusa é {:.2f}.'.format(a))

#ou
# b = float(input('Digite o valor do cateto oposto: '))
# c = float(input('Digite o valor do cateto adjacente: '))
# print('A hipotenusa é {:.2f}.'.format((b**2+c**2)**0.5)) sem importação de módulos

#ou
# import math
# b = float(input('Digite o valor do cateto oposto: '))
# c = float(input('Digite o valor do cateto adjacente: '))
# print('A hipotenusa é {:2f}.'.format(math.hypot(b,c))) função matemática para calcular a hipotenusa importanto o módulo math


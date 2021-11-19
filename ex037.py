#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
#de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input('Digite um número: '))
print('Para qual base você quer converter?\n[1]-Binário\n[2]-Octal\n[3]-Hexadecimal')
base = int(input('Digite a opção 1, 2 ou 3: '))
if base == 1:
    print('O valor em binário é: {}'.format(bin(num)[2:]))#usando o fatiamento de string para retirar 0b
elif base == 2:
    print('O valor em octal é: {}'.format(oct(num)[2:]))#usando o fatiamento de string para retirar 0o
elif base == 3:
    print('O valor em hexadecimal é {}'.format(hex(num)[2:]))#usando o fatiamento de string para retirar 0x
else:
    print('Valor inválido. Favor insira uma das três opções.')






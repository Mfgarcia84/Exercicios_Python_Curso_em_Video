#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('{} é ano bissexto.'.format(ano))
else:
    print('{} não é ano bissexto.'.format(ano))










#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando
#R$ 0,50 por km para viagens de até 200km e R$0,45 para viagens maiores.

dist = float(input('Digite a distância em km: '))
if dist <= 200:
    print('Vaigem mais curta. O valor da passagem é R${}'.format(dist*0.5))
else:
    print('Viagem mais longa. O valor de passagem é R${}'.format(dist*0.45))

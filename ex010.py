#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considere US$1.00=R$3.27
print()
print('='*50,'DESAFIO 010','='*50)
real = float(input('Digite o valor em real: (R$) '))
real_to_dolar = real/3.27
print('Você pode comprar US${:.2f} dólar(es).'.format(real_to_dolar))



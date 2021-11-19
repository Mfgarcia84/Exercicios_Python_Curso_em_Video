#Escreva um programa que leia um valor em metros e exiba convertido em centímetrose milímetros
print()
print('='*50,'DESAFIO 008','='*50)
valor = float(input('Digite o valor em metros (m): '))
#print(type(valor))
cm = valor * 100
mm = valor * 1000
print('{} metro(s) equivale(m) a {:.0f} centímetro(s) e {:.0f} milímetro(s).'.format(valor,cm,mm))


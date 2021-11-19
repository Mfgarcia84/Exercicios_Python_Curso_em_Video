#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#ex
#Digite um número:1834
#uniddade:4
#dezena:3
#centena:8
#milhar:1

# num = int(input('Digite um número entre 0 e 9999: '))
# div = str(num/1000)
# print(div)
# print('A unidade é: {}'.format(div.split()[0][4]))
# print('A dezena é: {}'.format(div.split()[0][3]))
# print('A centena é: {}'.format(div.split()[0][2]))
# print('O milhar é: {}'.format(div.split()[0][0]))

num = int(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(num//1%10))
print('Dezena: {}'.format(num//10%10))
print('Centena: {}'.format(num//100%10))
print('Milhar: {}'.format(num//1000%10))












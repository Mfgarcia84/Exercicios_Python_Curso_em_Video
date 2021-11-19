#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
print()
print('='*50,'DESAFIO 012','='*50)
preco = float(input('Digite o preço do produto: R$ '))
preco_c_desconto = preco - preco*0.05
print('\nO preço do produto com desconto é R$ {:.2f}'.format(preco_c_desconto))


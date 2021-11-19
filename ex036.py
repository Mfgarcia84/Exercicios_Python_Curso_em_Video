#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal. Sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Informe o valor do imóvel: R$'))
salario = float(input('Informe o salário do comprador: R$'))
tempo = float(input('Quantos anos de financiamento? '))
mensalidade = valor / tempo / 12
print(mensalidade)
if mensalidade > (salario*0.30):
    print('Seu financiamento não foi aprovado.')
else:
    print('Seu financiamento foi aprovado e sua mensalidade será de R$ {:.2f}.'.format(mensalidade))

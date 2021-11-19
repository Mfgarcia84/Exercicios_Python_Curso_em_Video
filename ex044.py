#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal
#e condição de pagamento.
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS GARCIA '))
preco = float(input('Digite o preço da compra: R$'))
#print('FORMAS DE PAGAMENTO:\n[1] à vista dinheiro/cheque\n[2] à vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
#ou
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

pagamento = int(input('Escolha uma das quatro opções: '))
if pagamento == 1:
    print('Para pagamento à vista dinheiro/cheque, tem desconto de 10%. O valor da compra sai a R${:.2f}.'.format(preco-preco*0.10))
elif pagamento == 2:
    print('Para pagamento à vista no cartão, tem desconto de 5%. O valor da compra sai a R${:.2f}'.format(preco-preco*0.05))
elif pagamento == 3:
    print('Para pagamento até 2x no cartão, não tem desconto. O valor da compra sai a R${:.2f}.'.format(preco))
elif pagamento == 4:
    opcao_parcelamento = int(input('Quantas parcelas? '))
    valor_parcela = (preco + preco * 0.20) / opcao_parcelamento
    print('Sua compra será parcelada em {} vezes de R${:.2f} com juros.'.format(opcao_parcelamento,valor_parcela))
    print('Sua compra de R${} custará R${}.'.format(preco,(valor_parcela*opcao_parcelamento)))
else:
    print('\033[1:31mOpção inválida. Digite uma opção de 1 a 4.\033[]')
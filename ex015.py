#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar. Sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
print()
print('='*50,'DESAFIO 015','='*50)
d = int(input('Digite a quantidade de dias alugados: (dias) '))
km = float(input('Digite a quantidade de kilômetros percorridos: (km) '))
print ('Você alugou o carro por {} dia(s) e rodou {} km. O valor de aluguel a ser pago é R${:.2f}.'.format(d,km,(d*60+km*0.15)))
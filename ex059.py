'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite outro número: '))
print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair')
opcao = int(input('Qual operação você deseja realizar? '))
while 1 <= opcao <= 5:
    if opcao == 1:
        soma = num_1 + num_2
        print('A soma entre {} e {} é {}'.format(num_1,num_2,soma))
    if opcao == 2:
        multiplicacao = num_1 * num_2
        print('A multiplicação entre {} e {} é {}'.format(num_1,num_2,multiplicacao))
    if opcao == 3:
        maior = max(num_1,num_2)
        print('O maior número entre {} e {} é {}'.format(num_1,num_2,maior))
    if opcao == 4:
        num_1 = float(input('Digite um número: '))
        num_2 = float(input('Digite outro número: '))
    if opcao == 5:
        
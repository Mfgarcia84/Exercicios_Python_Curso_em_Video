'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''



n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
encerrar = False
while not encerrar:
        print('Qual operação você deseja realizar com estes números? \n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR')
        operacao = int(input('Digite a opção desejada: '))
        if operacao == 1:
            soma = n1 + n2
            print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
        elif operacao == 2:
            multiplicacao = n1 * n2
            print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multiplicacao))
        elif operacao == 3:
            if n1 > n2:
                print('O maior número entre {} e {} é {}.'.format(n1, n2, n1))
            if n2 > n1:
                print('O maior número entre {} e {} é {}.'.format(n1, n2, n2))
            if n2 == n1:
                print('O números {} e {} são iguais.'.format(n1, n2))
        elif operacao == 4:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
        elif operacao == 5:
            encerrar = True
        else:
            print('Opção inválida. Digite uma opção de 1 a 5.')
print('FIM')





















'''import time
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
sair = False
while not sair:
    time.sleep(1)
    print('-='*20)
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1,n2,soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1,n2,multiplicacao))
    elif opcao == 3:
        maior = max(n1,n2)
        print('O maior valor entre {} e {} é {}.'.format(n1,n2,maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        sair = True
    else:
        print('Opção inválida! Digite uma das opções.')
print('Finalizando...')
time.sleep(2)
print('FIM')'''

# import time
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
#
# condicao =  False
# while not condicao:
#     opcao = int(input('Digite uma opção: '))
#     if opcao == 1:
#         soma = n1 + n2
#         print('\033[31mVocê escolheu a opção {}, soma. A soma entre {} e {} é {}.\033[m'.format(opcao,n1,n2,soma))
#         time.sleep(3)
#         print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
#     if opcao == 2:
#         multiplicacao = n1 * n2
#         print('\033[31mVocê escolheu a opção {}, multiplicação. A multiplicação entre {} e {} é {}\033[m.'.format(opcao,n1,n2,multiplicacao))
#         time.sleep(3)
#         print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
#     if opcao == 3:
#         if n1 > n2:
#             print('\033[31mVocê escolheu a opção {}, maior. O maior número entre {} e {} é {}.\033[m'.format(opcao,n1,n2,n1))
#             time.sleep(3)
#             print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
#         if n2 > n1:
#             print('\033[31mVocê escolheu a opção {}, maior. O maior número entre {} e {} é {}.\033[m'.format(opcao,n1,n2,n2))
#             time.sleep(3)
#             print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
#         if n1 == n2:
#             print('\033[31mVocê escolheu a opção {}, maior. Os números digitados são iguais.\033[m'.format(opcao))
#             time.sleep(3)
#             print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
#     if opcao == 4:
#         print('\033[31mVocê escolheu a opção {}, novos números. Escolha dois novos números.\033[m'.format(opcao))
#         n1 = int(input('Digite um número: '))
#         n2 = int(input('Digite outro número: '))
#         print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
#     if opcao not in (1,2,3,4,5):
#         print('Opção Inválida. Digite uma opção de 1 a 5.')
#     if opcao == 5:
#         condicao = True
# print('FIM')
















'''n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair')
opcao = int(input('Qual operação você deseja realizar? '))
while 1 <= opcao <= 5:
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    if opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1,n2,multiplicacao))
    if opcao == 3:
        maior = max(n1,n2)
        print('O maior número entre {} e {} é {}'.format(n1,n2,maior))
    if opcao == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    if opcao == 5:'''

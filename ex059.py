'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

#minha solução
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
encerrar = False
while not encerrar:
    print('~'*35)
    print('Qual operação você deseja fazer? \n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair')
    print('~'*35)
    opcao = int(input('>>>>> Digite uma opção: '))
    if opcao == 1:
        s = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, s))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, mult))
    elif opcao == 3:
        maior = max(n1, n2)
        print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
        encerrar = True
    else:
        print('Opção inválida!')
    sleep (1)
print('FIM')
    
'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag, ou seja, não considerar o 999 na soma)'''

encerrar = False
soma = 0
cont = 0
while not encerrar:
    num = int(input('Digite um número: '))
    if num == 999:
        encerrar = True
    else:
        soma = soma + num
        cont = cont + 1
print('A quantidade de números digitados foi {}'.format(cont))
print('A soma entre os números digitados é {}.'.format(soma))


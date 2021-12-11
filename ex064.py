'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag, ou seja, não considerar o 999 na soma)'''

c = 0
s = 0
encerra = False
while not encerra:
    num = int(input('Digite um número: '))
    if num != 999:
        c = c + 1
        s = s + num
    if num == 999:
        encerra = True
print('Você digitou {} número(s) e a soma entre eles é {}.'.format(c, s))


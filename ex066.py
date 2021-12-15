'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

#minha solução = solução da aula
c = s = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    c = c + 1
    s = s + num
print(f'Você digitou {c} números. E a soma entre eles é {s}.')


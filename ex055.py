#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(c)))
    if c == 1: #se for o primeiro laço que estiver ocorrendo (primeira ocorrência) então o valor do peso será o maior e o menor peso.
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso informado é {}kg.'.format(maior))
print('O menor peso informado é {}kg.'.format(menor))


# maior = 0
# menor = 0
# for c in range(1,6):
#     peso = float(input('Digite o peso da {}ª pessoa em kg:  '.format(c)))
#     if c == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
#
# print('O maior peso é {}.'.format(maior))
# print('O menor peso é {}.'.format(menor))
















# maior = 0
# menor = 0
# for p in range(1, 6): #p é á variável que receberá valores de 1 a 5
#     peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print('O maior peso lido foi de {}kg.'.format(maior))
# print('O menor peso lido foi de {}kg.'.format(menor))
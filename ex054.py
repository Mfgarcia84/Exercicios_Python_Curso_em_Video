#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
#não atingiram a maioridade e quantas já são maiores.


import datetime
s = 0
t = 0
ano_atual = datetime.date.today().year
for c in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano_atual - ano_nascimento >= 18:
        t = t + 1
    else:
        s = s + 1
print('{} pessoa(s) já atingiram a maioridade.'.format(t))
print('{} pessoa(s) ainda não atingiram a maioridade.'.format(s))


# import datetime
# data_atual = datetime.date.today().year
# maior = 0
# menor = 0
# for c in range(1, 8):
#     ano_nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
#     if data_atual - ano_nascimento >= 18:
#         maior = maior + 1
#     else:
#         menor = menor + 1
# print('A quantidade de pessoas na maioridade é {}.'.format(maior))
# print('A quantidade de pessoas na menoridade é {}.'.format(menor))



# import datetime
# ano_atual = datetime.date.today().year
# s = 0
# t = 0
# for c in range(1, 8):
#     ano_nascimento = int(input('Digite o ano de nascimento: '))
#     idade = ano_atual - ano_nascimento
#     if idade >= 21:
#         s = s + 1
#     else:
#         t = t + 1
# print('{} pessoas já atingiram a maioridade e {} pessoas ainda não atingiram a maioridade.'.format(s, t))


# import datetime
# p1 = int(input('Digite o ano de nascimento: '))
# p2 = int(input('Digite o ano de nascimento: '))
# p3 = int(input('Digite o ano de nascimento: '))
# p4 = int(input('Digite o ano de nascimento: '))
# p5 = int(input('Digite o ano de nascimento: '))
# p6 = int(input('Digite o ano de nascimento: '))
# p7 = int(input('Digite o ano de nascimento: '))
# data = datetime.date.today().year
#
# if data - p1 >= 18:
#     print('A pessoa 1 atingiu maioridade.')
# else:
#     print('A pessoa 1 não atingiu a maioridade.')
# if data - p2 >= 18:
#     print('A pessoa 2 atingiu a maioridade.')
# else:
#     print('A pessoa 2 não atingiu a maioridade.')
#

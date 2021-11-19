#Desenvolva um program que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo
#qual é o nome do homem mais velho
#quantas mulheres tem menos de 20 anos.

t = 0
soma_idade = 0
velho = 0
nome_mais_velho = ''
for c in range(1, 5):
    print("-="*7,'{}ª PESSOA'.format(c),'-='*7)
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).replace(' ','').upper()
    soma_idade = idade + soma_idade
    if sexo == 'M':
        if idade > velho:
            velho = idade
            nome_mais_velho = nome
    else:
        if idade < 20:
            t = t + 1
media_idade = soma_idade / c
print('A média de idade do grupo é de {:.0f} anos.'.format(media_idade))
print('O nome do homem mais velho é {}.'.format(nome_mais_velho))
print('As quantidade de mulheres abaixo de 20 anos é: {}'.format(t))


#
# nomevelho = ''
# velho = 0
# s = 0
# t = 0
# for c in range(1, 5):
#     print('-'*10,'{}ª PESSOA'.format(c),'-'*10)
#     nome = str(input('Nome: ')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo [M/F]: ')).strip().upper()
#     s = s + idade
#     if sexo == 'F' and idade < 20:
#         t = t + 1
#     if sexo in 'Mm': #in substitui == e o usuário pode digitar M ou m (maiúsculo ou minúsculo)
#         if idade > velho:
#             velho = idade
#
# print('A média de idade do grupo é de {:.0f} anos.'.format(s / c))
# print('O homen mais velho tem {} anos e se chama {}'.format(velho,nome))
# print('O número de mulheres abaixo de 20 anos é {}.'.format(t))
#


# t = 0
# soma_idade = 0
# for c in range(1, 5):
#     nome = str(input('Digite o nome: '))
#     idade = int(input('Digite a idade: '))
#         if idade >
#     sexo = str(input('Digite o sexo: '))
#     soma_idade = soma_idade + idade
#     t = t + 1
# #print(soma_idade)
# med_idade = soma_idade / t
# print('A média de idade do grupo é {:.1f}'.format(med_idade))


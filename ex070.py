'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar. 
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$1000
c) qual é o nome do produto mais barato'''

#minha solução
'''soma = c = cont = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    soma = soma + preco
    cont = cont + 1
    if preco > 1000:
        c = c + 1
    if cont == 1:
        mais_barato = preco
        produto_mais_barato = nome
    if cont > 1:
        if preco < mais_barato:
            mais_barato = preco
            produto_mais_barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).replace(' ','').upper()[0]
    if continuar == 'N':
        break
print('~'*50)
print(f'O total da compra foi R$ {soma:.2f}.')
print(f'Temos {c} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato é {produto_mais_barato} e custa R$ {mais_barato}.')
print('~'*50)'''

#solução da aula
soma = c = cont = 0
produto_mais_barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    soma = soma + preco
    cont = cont + 1
    if preco > 1000:
        c = c + 1
    if cont == 1 or preco < mais_barato: # "or" precisa de uma única premissa verdadeira para executar o bloco
        mais_barato = preco
        produto_mais_barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).replace(' ','').upper()[0]
    if continuar == 'N':
        break
print('~'*50)
print(f'O total da compra foi R$ {soma:.2f}.')
print(f'Temos {c} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato é {produto_mais_barato} e custa R$ {mais_barato}.')
print('~'*50)
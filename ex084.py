"""
Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
"""

dados = list()
pessoas = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0: #o if entra aqui porque essa posição é a primeira evidência do peso.
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    reposta = ' '
    pessoas.append(dados[:])
    dados.clear()
    while reposta not in 'SN':
        reposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if reposta == 'N':
        break
print(pessoas)
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi {maior}: ',end='')
for c in pessoas:
    if c[1] == maior:
        print(f'[{c[0]}]',end='')
print(f'\nO menor peso cadastrado foi {menor}: ', end='')
for c in pessoas:
    if c[1] == menor:
        print(f'[{c[0]}]', end='')



#minha solução
'''nome_mais_pesado = list()
nome_mais_leve = list()
for c in range(len(pessoas)):
    if c == 0:
        maior_peso = menor_peso = pessoas[c][1]
        nome_mais_pesado.append(pessoas[c][0])
        nome_mais_leve.append(pessoas[c][0])
    else:
        if pessoas[c][1] >= maior_peso:
            if pessoas[c][1] > maior_peso:
                maior_peso = pessoas[c][1]
                nome_mais_pesado.clear()
                nome_mais_pesado.append(pessoas[c][0])
            else:
                nome_mais_pesado.append(pessoas[c][0])
        elif pessoas[c][1] <= menor_peso:
            if pessoas[c][1] < menor_peso:
                menor_peso = pessoas[c][1]
                nome_mais_leve.clear()
                nome_mais_leve.append(pessoas[c][0])
            else:
                nome_mais_leve.append(pessoas[c][0])


print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'maior peso é {maior_peso}: {nome_mais_pesado}')
print(f'menor peso é {menor_peso}: {nome_mais_leve}')'''


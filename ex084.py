"""
Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
"""

dados = list()
pessoas = list()
cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    cont = cont + 1
    reposta = ' '
    pessoas.append(dados[:])
    dados.clear()
    while reposta not in 'SN':
        reposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if reposta == 'N':
        break
print(pessoas)
nome_mais_pesado = list()
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
        elif pessoas[c][1] < menor_peso:
            menor_peso = pessoas[c][1]
            nome_mais_leve.clear()
            nome_mais_leve.append(pessoas[c][0])

print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'maior peso é {maior_peso}: {nome_mais_pesado}')
print(f'menor peso é {menor_peso}: {nome_mais_leve}')


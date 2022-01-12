'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas
b) a média de idade do grupo
c) uma lista com todas as mulheres
d) uma lista com todas as pessoas com idade acima da média
'''


dados_pessoa  = {} #dicionário
dados_geral = [] #lista
while True:
    dados_pessoa['nome'] = str(input('Nome: '))
    while True:
        dados_pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados_pessoa['sexo'] not in 'MF':
            print('Erro! Por favor digite apenas M ou F.')
        else:
            break
    dados_pessoa['idade'] = int(input('Idade: '))
    dados_geral.append(dados_pessoa.copy()) #copia o dicionário para dentro da lista (semelhante ao comando [:])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resposta == 'N':
        break
print(dados_geral)
soma_idade = 0
for i in range(len(dados_geral)):
    idade = dados_geral[i]['idade']
    soma_idade = soma_idade + idade
media = soma_idade/len(dados_geral)

print(f'A) Ao todo temos {len(dados_geral)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.1f} anos.')
print('C) As mulheres cadastradas foram: ',end='')
for i in dados_geral:
    if i['sexo'] == 'F':
        print(i["nome"], end=' ')
print()
print('D) Listas das pessoas que estão com idade acima da média: ')

for d in dados_geral:
    if d['idade'] > media:
        for k, v in d.items():
            print(f'{k} = {v};', end=' ')
    print()


'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas
b) a média de idade do grupo
c) uma lista com todas as mulheres
d) uma lista com todas as pessoas com idade acima da média
'''


pessoa = {} #dicionário
galera = [] #lista
while True:
    #pessoa.clear() - não precisa do comando, pois os valores das chaves 'nome', 'sexo' e 'idade' estão sendo substituídos a cada volta
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] not in 'MF':
            print('Erro! Por favor digite apenas M ou F.')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy()) #copia o dicionário para dentro da lista (semelhante ao comando [:])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resposta == 'N':
        break
print(galera)
soma_idade = 0
for i in range(len(galera)):
    idade = galera[i]['idade']
    soma_idade = soma_idade + idade
media = soma_idade/len(galera)

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.1f} anos.')
print('C) As mulheres cadastradas foram: ',end='')
for mulher in galera:
    if mulher['sexo'] == 'F':
        print(mulher["nome"], end=' ')
print()
print('D) Listas das pessoas que estão com idade acima da média: ')
for d in galera:
    if d['idade'] > media:
        for k, v in d.items():
            print(f'{k:>10} = {v};', end='')
    print()


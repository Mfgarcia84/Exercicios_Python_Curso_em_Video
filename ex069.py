'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos'''

#minha solução = solução da aula
c = maior_idade = qtd_homens = qtd_mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' ' #sexo vazio para entrar no while
    c = c + 1
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo: [M/F] ')).replace(' ','').upper()[0]
    if idade > 18:
        maior_idade = maior_idade + 1
    if sexo == 'M':
        qtd_homens = qtd_homens + 1
    if sexo == 'F' and idade < 20:
        qtd_mulheres = qtd_mulheres + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).replace(' ','').upper()[0]
    if continuar == 'N':
        break
print('~'*40)
print(f'{c} pessoas foram cadastradas.')
print(f'{maior_idade} pessoa(s) tem mais de 18 anos.')
print(f'{qtd_homens} homem(ns) foram cadastrados.')
print(f'{qtd_mulheres} mulher(es) tem menos de 20 anos.')
print('~'*40)

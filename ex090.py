'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em
um dicionário (média > 7 aprovado ou média < 7 reprovado). No final, mostre o conteúdo da estrutura na tela.
'''

dadosaluno = {}
while True:
    dadosaluno['Nome'] = str(input('Nome: '))
    dadosaluno['Média'] = float(input('Média: '))
    if dadosaluno['Média'] > 7:
        dadosaluno['Situação'] = 'Aprovado'
    else:
        dadosaluno['Situação'] = 'Reprovado'
    break
print(dadosaluno)
for k, v in dadosaluno.items():
    print(f'{k} é igual a {v}')



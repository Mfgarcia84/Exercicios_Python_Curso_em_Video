'''
Crie um programa que leia nome, ano de nascimento, e carteira de trabalho, e cadastre-os (guarde a idade e
não o ano de nascimento) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai
se aposentar (se aposenta com 35 anos de colaboração).
'''

#solução aula

from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = datetime.now().year
dados['idade'] = ano_atual - ano_nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contratação'] + 35) - ano_atual + dados['idade']
print(dados)


#minha solução
'''from datetime import datetime
ano_atual = datetime.now().year

dic = {}
nome = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps <= 0:
    dic['nome'] = nome
    dic['idade'] = ano_atual - anonasc
    dic['ctps'] = ctps
else:
    contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$ '))
    dic['Nome'] = nome
    dic['idade'] = ano_atual - anonasc
    dic['ctps'] = ctps
    dic['contratação'] = contratacao
    dic['salário'] = salario
    dic['aposentadoria'] = (int(dic['contratação']) + 35) - ano_atual + dic['idade'] #idade que a pessoa vai se aposentar
for k, v in dic.items():
    print(f'- {k} tem o valor {v}')
'''


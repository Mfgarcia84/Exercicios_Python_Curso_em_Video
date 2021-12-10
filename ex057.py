'''ex057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto'''

c = False
while not c:
    sexo = str(input('Informe o sexo: [M/F] '))
    if sexo == 'M' or sexo == 'F':
        c = True
    else:
        print('Opção inválida. Informe o sexo corretamente.')
print('O sexo é {}.'.format(sexo))


'''sexo = str(input('Informe seu sexo: ')).replace(' ','').upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).replace(' ','').upper()
print('O sexo é: {}'.format(sexo))'''


# sexo = str(input('Informe o sexo: '))
# while sexo != 'M' and sexo != 'F': #while sexo in 'MmFf':
#     sexo = str(input('Dados inválidos. Por favor informe o sexo novamente: [M/F] '))
# if sexo == 'M':
#     print('A pessoa é do sexo Masculino.')
# else:
#     print('A pessoa é do sexo Feminino.')

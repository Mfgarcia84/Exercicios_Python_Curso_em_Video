'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto'''

#minha solução
encerrar = False
while not encerrar:
    sexo = str(input('Informe o sexo: [M/F] ')).replace(' ','').upper()[0]
    if sexo == 'M' or sexo == 'F':
        encerrar = True
    else:
        print('Opção inválida. Tente outra vez.')
print('O sexo escolhido foi o "Masculino".' if sexo == 'M' else 'O sexo escolhido foi o "Feminino".')


#solução aula
'''sexo = str(input('Digite seu sexo: [M/F] ')).replace(' ','').upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção inválida. Digite o sexo: '))
print('Sexo Masculino cadastrado com sucesso' if sexo in 'Mm' else 'Sexo Feminino cadastrado com sucesso.')'''



#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas.
#o nome com todas as letras minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite o nome completo: '))
print(len(nome))
print('O nome com letras maiúsculas é: {}'.format(nome.upper()))
print('O nome com letras minúsculas é: {}'.format(nome.lower()))
print('O nome tem ao todo {} caracteres sem espaço.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras.'.format(len(nome.split()[0]))) #ou print(nome.find(' '))















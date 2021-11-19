#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
#separadamente.
#ex: Ana Maria de Souza
#primeiro: Ana
#último: Souza
nome = str(input('Digite o nome completo: ')).strip()
#print(nome.split())
#print(len(nome.split()))
print('O primeiro nome é: {}'.format(nome.split()[0]))
print('O último nome é: {}'.format(nome.split()[len(nome.split())-1]))






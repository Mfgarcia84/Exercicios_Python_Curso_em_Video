#crie um programa que leia o nome de uma  pessoa e diga se ela tem "SILVA" no nome.
# nome = str(input('Digite o nome completo: ').upper())
# bol = 'SILVA' in nome

nome = str(input('Digite o nome da pessoa: ')).strip().upper()
if 'SILVA' in nome:
    print('Tem "SILVA" no nome.')
else:
    print('Não tem "SILVA" no nome.')
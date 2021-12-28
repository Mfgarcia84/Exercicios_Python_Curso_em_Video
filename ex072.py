'''Crie um programa que tenha uma tupla totalmente preenchida com um contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove','Dez', 'Onze', 'Doze', 'Treze',
'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))
num_escolhido = lista[num]
print(f'Você escolheu o número "{num_escolhido}"')

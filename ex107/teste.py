'''
Ex: 107
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().Faça também um programa que esse módulo e use
algumas dessas funções.
'''


from ex111.UtilidadesCeV import moeda
preco = float(input('Digite o preço: R$ '))
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(preco, 13)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')
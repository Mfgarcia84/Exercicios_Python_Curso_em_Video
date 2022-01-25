'''
Ex: 108
Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.
'''


from ex111.UtilidadesCeV import moeda
preco = float(input('Digite o preço: R$ '))
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10), "R$")}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.reduzir(preco, 13), "R$")}')
print(f'O dobro de {moeda.moeda(preco, "R$")} é {moeda.moeda(moeda.dobro(preco), "R$")}')
print(f'A metade de {moeda.moeda(preco, "R$")} é {moeda.moeda(moeda.metade(preco), "R$")}')
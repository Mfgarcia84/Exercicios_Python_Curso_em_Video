'''
Ex: 109
Modifique as funções que foram criadas no desafio ex107 para que elas aceitem um
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado
pela função moeda(), desenvolvida no desafio 108.
'''


from ex111.UtilidadesCeV import moeda
preco = float(input('Digite o preço: R$ '))
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, formatar=True)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(preco, 13, formatar=True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, formatar=True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, formatar=True)}')
'''
Ex 112
Dentro do pacote UtilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
chamda leiadinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados
para aceitar apenas valores que sejam monetários
'''

from ex112.UtilidadesCeV import dado, moeda
preco = dado.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 80, 35)



















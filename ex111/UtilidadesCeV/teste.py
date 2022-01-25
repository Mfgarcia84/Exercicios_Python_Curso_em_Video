'''
Ex. 111
Crie um pacote chamado UtilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote
e mantenha tudo funcionando.
'''
from ex111.UtilidadesCeV import moeda
preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 20, 12) #80 percentual de aumento e 35 percentual de redução


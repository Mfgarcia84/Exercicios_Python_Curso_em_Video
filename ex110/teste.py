'''
Ex: 110
Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chaamda resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado
até aqui.
'''


from ex111.UtilidadesCeV import moeda
preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 20, 12) #80 percentual de aumento e 35 percentual de redução


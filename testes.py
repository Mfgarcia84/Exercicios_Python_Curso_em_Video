'''board = []

for i in range(8):#parte exterior constroi 8 linhas
    row = ['EMPTY' for c in range(8)] #parte interior constroi uma linha com 8 colunas
    board.append(row)

#ou
board = [[EMPTY for i in range(8)] for j in range(8)]
#parte interior constroi uma linha com 8 colunas (ordem de precedencia)
#parte exterior constroi 8 linhas'''

#GRAVAR PARA ENUMERATE
'''comidas = [['pizza', 'refrigerante'], ['pipoca', 'suco']] #listas são variáveis compostas
for a, b in enumerate(comidas): #"a" e "b" são variáveis simples. E eu quero atribuir valores a "a" e "b" a partir da lista
    print(a,b)
#enumarate são tuplas contendo indice e o valor (sempre gera dupla de valores).    
#output
0 ['pizza', 'refrigerante']
1 ['pipoca', 'suco']'''


'''lista = [['marcelo', 6.0, 7.0, 6.5], ['thamiris', 8.0, 9.0, 8.5], ['renato', 4.0, 5.0, 4.5], ['lainho', 9.0, 0.0, 4.5]]

print('-='*17)
print(f'{"NOME":<10}', f'{"NOTA 1":<8}', f'{"NOTA 2":<8}', f'{"MÉDIA":>5}')
print('-='*17)

for a, b in enumerate(lista):
    print(f'{b[0]:<10}', f'{b[1]:<8}', f'{b[2]:<8}', f'{b[3]:>5}')
print('-='*17)'''

#Dicionário => os índices são substuídos por nomes
#são representados por chaves {}
#Ex:

#dados = dict()
#dados = {}

'''dados = {'nome':'marcelo', 'idade':25} #marcelo é o valor e nome é o identificador (assim como os indices)
print(dados['nome'], dados['idade'])'''



'''pessoas = {'Nome':'Marcelo', 'Idade':37, 'Sexo':'M'}
pessoas['Nome'] = 'Thamiris' #substituindo valores
pessoas['Idade'] = 34 #substituindo valores
pessoas['Sexo'] = 'F' #substituindo valores
pessoas['Peso'] = 50 #adicionando valores
#acessado os values, keys e items através de "for"
for k, v in pessoas.items(): #para cada key dentro de pessoas.keys(), onde pessoas.keys() são: 'Nome', 'Idade' e 'Sexo'
    print(f'{k} = {v}')'''


estado = {}
brasil = []
for i in range(3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')














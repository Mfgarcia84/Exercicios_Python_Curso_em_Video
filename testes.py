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
    
#output
0 ['pizza', 'refrigerante']
1 ['pipoca', 'suco']'''


lista = [['marcelo', 6.0, 7.0, 6.5], ['thamiris', 8.0, 9.0, 8.5], ['renato', 4.0, 5.0, 4.5], ['lainho', 9.0, 0.0, 4.5]]

print('-='*17)
print(f'{"NOME":<10}', f'{"NOTA 1":<8}', f'{"NOTA 2":<8}', f'{"MÉDIA":>5}')
print('-='*17)

for a, b in enumerate(lista):
    print(f'{b[0]:<10}', f'{b[1]:<8}', f'{b[2]:<8}', f'{b[3]:>5}')
print('-='*17)
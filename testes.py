'''board = []

for i in range(8):#parte exterior constroi 8 linhas
    row = ['EMPTY' for c in range(8)] #parte interior constroi uma linha com 8 colunas
    board.append(row)

#ou
board = [[EMPTY for i in range(8)] for j in range(8)]
#parte interior constroi uma linha com 8 colunas (ordem de precedencia)
#parte exterior constroi 8 linhas'''

casal = [['marcelo', 'thamiris'],['lainho', 'natalia'], ['renato', 'thais']]
print(enumerate(casal))



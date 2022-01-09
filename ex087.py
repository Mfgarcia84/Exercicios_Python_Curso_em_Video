''''
Ex. 086
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
------------------------------------------------------------------------------------------------
Ex. 087
Aprimore o desafio anterior (ex86), mostrando no final:
a) a soma de todos os valores pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha
'''

lista3coluna = []
listapar = []
lista = []
for l in range(3):
    coluna = [(int(input(f'Digite um valor para [{l},{c}]: '))) for c in range(3)]
    for i in coluna:
        if i % 2 == 0:
            listapar.append(i)
    lista.append(coluna)

for l in range(3):
    for c in range(3):
        if c == 2:
            lista3coluna.append(lista[l][c])

print('-='*13)
for l in range(3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]',end=' ')
    print()
print('-='*13)
print(f'A soma dos valores pares é: {sum(listapar)}')
print(f'A soma de terceira coluna da matriz é: {sum(lista3coluna)}')
print(f'O maior valor da segunda linha é: {max(lista[1])}')

"""
Ou para somar a terceira coluna
soma_coluna_3 = 0
for l in range(3):
    soma_coluna_3 = soma_coluna_3 + lista[l][2]
"""

"""
mai = 0
Ou para maior valor da segunda linha
for c in range(3):
    if c == 0:
        mai = lista[1][c]
    elif lista[1][c] > mai:
        mai = lista[1][c]
"""
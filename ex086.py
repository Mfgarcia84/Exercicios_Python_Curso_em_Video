'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''


matriz = []
for l in range(3):
    coluna = [int(input(f'Digite um valor para [{l},{c}]: ')) for c in range(3)]
    matriz.append(coluna)
print(matriz)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()



'''for l in range(3):
print(f'[{matriz[p][0]}] [{matriz[p][1]}] [{matriz[p][2]}]')'''









'''lista = [[],[],[]]
for c in range(3):
    valor = int(input(f'Digite um valor para [0,{c}]: ' ))
    lista[0].append(valor)
for c in range(3):
    valor = int(input(f'Digite um valor para [1,{c}]: '))
    lista[1].append(valor)
for c in range(3):
    valor = int(input(f'Digite um valor para [2,{c}]: '))
    lista[2].append(valor)
print(f'{lista[0]}')
print(lista[1])
print(lista[2])'''
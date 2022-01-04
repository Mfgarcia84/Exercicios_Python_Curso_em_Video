"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenanda na tela.
"""

lista_num = list()
for c in range(5):
    num = int(input(f"Digite o {c+1}º número: "))
    if c == 0:
        lista_num.append(num)
    elif num >= lista_num[-1]:
        lista_num.append(num)
    else:
        pos = 0
        while pos < len(lista_num):
            if num <= lista_num[pos]:
                lista_num.insert(pos, num)
                break
            pos = pos + 1
print(lista_num)

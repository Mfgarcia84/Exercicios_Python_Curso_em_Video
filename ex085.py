'''
Crie um programa onde um usuário possa digitar 7 valores numéricos e cadastre-o em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente.
'''


num = [[],[]]
for i in range(1, 8):
    n = int(input(f'Digite o {i}ª número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Os números pares digitados foram: {num[0]}')
print(f'Os números impares digitados foram: {num[1]}')

"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem dos números gerados e também indique o menor e o maior 
valor que estão na tupla"""

# opção sem transformar tupla em lista
from random import randint

lista = (
    randint(0, 1000),
    randint(0, 1000),
    randint(0, 1000),
    randint(0, 1000),
    randint(0, 1000),
)
print("Os valores sorteados são: ", end="")
for i in range(len(lista)):
    print(lista[i], "," if i <= 3 else "", end=" ")
print(f"\nO maior número sorteado: {max(lista)}")
print(f"O menor número sorteado: {min(lista)}")


# opção transformando tupla em lista
"""from random import randint
lista = ()
nova_lista = list(lista)
for i in range(0, 5):
    numero = randint(0,1000)
    nova_lista.append(numero)
print(f'Os valores sorteados foram: {nova_lista[0:5]}')
print(f'O maior número sorteado: {max(nova_lista)}')
print(f'O menor número sorteado: {min(nova_lista)}')"""

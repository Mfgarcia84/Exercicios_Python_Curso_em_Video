"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista"""

numeros = list()
for i in range(5):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))
maior = max(numeros)
menor = min(numeros)
print(f"\nVocê digitou os valores {numeros}")
print(f"O maior número digitado foi {maior} nas posições:", end=" ")
for p, v in enumerate(numeros):
    if v == maior:
        print(f"{p}..", end=" ")
print(f"\nO menor número digitado foi {menor} nas posições ", end=" ")
for p, v in enumerate(numeros):
    if v == menor:
        print(f"{p}..", end=" ")


# outra opção (apenas a parte do maior e menor)
"""numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    if i == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f"O maior número digitado foi: {maior} e sua posição é: {numeros.index(maior)}")
print(f"O menor número digitado foi: {menor} e sua posição é: {numeros.index(menor)}")
"""

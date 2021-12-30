"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final mostre uma listagem de preços, organizando os dados em forma tabular."""

produtos = (
    "Mouse",
    150,
    "Laptop",
    7000,
    "Monitor",
    800,
    "Hub",
    175,
    "Capa Notebook",
    90,
    "Mochila",
    180.5,
    "Caderno",
    30,
    "Caneta",
    10,
    "Borracha",
    2.3,
    "Lapiseira",
    7,
    "Grafite",
    6.5,
    "Lousa",
    210,
)
print("==" * 21)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("==" * 21)
for i in range(len(produtos)):
    if i % 2 == 0:
        print(f"{produtos[i]:.<30}", end=" ")
    else:
        print(f"R${produtos[i]:>9.2f}")
print("==" * 21)

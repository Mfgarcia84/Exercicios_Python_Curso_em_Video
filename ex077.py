"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso você deve mostrar, para cada palavra, quais são as suas vogais"""

lista = (
    "Cerveja",
    "Tabaco",
    "Cigarro",
    "Mesa",
    "Escola",
    "Python",
    "Futebol",
    "Pagode",
    "Futsamba",
    "Marcelo",
    "Figueiredo",
    "Monitor",
    "Cadeira",
    "Fitbol",
    "Carro",
    "Velho",
    "Nina",
    "celular",
)


for palavra in lista:
    print(f"\nNa palavra {palavra.upper()} temos", end=" ")
    for letra in palavra:
        if letra in "AaEeIiOoUu":
            print(letra, end=" ")

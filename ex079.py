"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos 
digitados, em ordem crescente."""


# solução da aula
lista = list()
while True:
    numero = int(input("Digite um número: "))
    if numero not in lista:
        lista.append(numero)
        print("Número adicionado com sucesso.")
    else:
        print("Número existente. Não vou adicionar.")
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S/N]")).upper()[0]
    if continuar == "N":
        break
lista.sort()
print(f"Você digitou os números: {lista}")


# minha solução
"""lista_inicial = list()
lista_final = list()
encerrar = False
while not encerrar:
    numero = int(input("Digite um número: "))
    lista_inicial.append(numero)
    if lista_inicial.count(numero) == 1:
        lista_final.append(numero)
        print("Valor inserido com sucesso.")
    else:
        print("Valor duplicado. Não vou adicionar.")
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S/N] ")).upper()[0]
    if continuar == "N":
        break
# print(f"lista_inicial: {lista_inicial}")
lista_final.sort()
print(f"Você digitou os números: {lista_final}")"""

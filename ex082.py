"""Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso crie duas listas extras que vão conter apenas os valores pares
e os valores impares digitados, respectivamente. Ao final mostre o conteúdo das três 
listas geradas.
"""

lista = list()
lista_par = list()
lista_impar = list()
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja continuar? [S/N] ")).upper()[0]
    if parar == "N":
        break
for valor in lista:
    if valor % 2 == 0 and valor != 0:  # zero não é par nem ímpar
        lista_par.append(valor)
    elif valor % 2 != 0:
        lista_impar.append(valor)
print(f"A lista com os valores pares é: {lista_par}")
print(f"A lista com os valores ímpares é: {lista_impar}")

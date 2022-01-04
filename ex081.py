"""Crie um programa que vai ler vários números e colocar numa lista. Depois disso, mostre: 
a) quantos números foram digitados.
b) a lista de valores ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista
"""
c = 0
lista_num = list()
while True:
    num = int(input("Digite um número: "))
    c += 1
    lista_num.append(num)
    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja continuar? [S/N] ")).upper()[0]
    if parar == "N":
        break
print(f"Lista inicial: {lista_num}")
lista_num.sort(reverse=True)
print(f"Você digitou {c} números.")
print(f"A lista ordenada de forma decrescente é: {lista_num}")
if 5 in lista_num:
    print(f"O número 5 está na posição {lista_num.index(5)} da lista.")
else:
    print("O número 5 não foi digitado.")

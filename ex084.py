"""
Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves

"""
cont = 0
dados = list()
pessoas = list()
while True:
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    cont = cont + 1
    pessoas.append(dados[:])
    dados.clear()
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N] ")).upper()[0]
    if resposta == "N":
        break
mais_pesado = mais_leve = 0
for p in pessoas:
    if p == 0:  # erro aqui
        mais_pesado = mais_leve = p[1]
    elif p[1] > mais_pesado:
        mais_pesado = p[1]
        nome_pesado = p[0]
    elif p[1] < mais_leve:
        mais_leve = p[1]
        nome_leve = p[0]
print(pessoas)
print(f"Ao todo você cadastrou {cont} pessoas.")
print(f"O maior peso foi de {mais_pesado}kg. Peso de {nome_pesado}.")
print(f"O menor peso foi de {mais_leve}kg. Peso de .")

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

for c in range(len(pessoas)):
    if c == 0:
        mais_pesado = mais_leve = pessoas[c][1]
    elif pessoas[c][1] > mais_pesado:
        mais_pesado = pessoas[c][1]
    elif pessoas[c][1] < mais_leve:
        mais_leve = pessoas[c][1]

print(pessoas)
print(f"mais pesado tem {mais_pesado} kilos")
print(f"mais leve tem {mais_leve} kilos")

"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
c) quais foram os números pares"""

"""c = 0
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
num4 = int(input('Digite o 4º número: '))
numeros = (num1, num2, num3, num4)
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if numeros.count(3) == 0:
    print(f'O número 3 não foi digitado nenhuma vez.')
else:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição.')
for i in range(4):
    if numeros[i] % 2 == 0:
        c = c + 1
print(f'Você digitou {c} números pares.')"""

# solução da aula
c = 0
numeros = (  # construção da tupla
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: ")),
)
print(f"O número 9 apareceu {numeros.count(9)} vezes.")
if 3 not in numeros:
    print(f"O número 3 não foi digitado nenhuma vez.")
else:
    print(f"O número 3 apareceu na {numeros.index(3)+1}ª posição.")
for i in range(4):
    if numeros[i] % 2 == 0:
        c = c + 1
print(f"Você digitou {c} números pares.")

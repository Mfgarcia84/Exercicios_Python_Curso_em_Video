#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
#no intervalo de 1 até 500.

primeiro = int(input('Digite o primeiro número do intervalo: '))
ultimo = int(input('Digite o último número do intervalo: '))
s = 0
for num in range(primeiro, ultimo+1):
    if num % 2 == 1 and num % 3 == 0:
        s = s + num
print(s)

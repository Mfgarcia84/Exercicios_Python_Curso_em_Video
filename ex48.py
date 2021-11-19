#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
#no intervalo de 1 até 500.

#somador: s = s + 0
sum = 0
init_int = int(input('Digite o início do intervalo: '))
end_int = int(input('Digite o fim do intervalo: '))
for c in range(init_int, end_int+1):
    if c % 2 != 0 and c % 3 == 0: #atende a condição de ímpar e é múltiplo de 3
        sum = sum + c
        print(c,end=' ')
print('\n'+'A soma dos números ímpares múltiplos de 3 do intervalo é {}.'.format(sum))


# primeiro = int(input('Digite o primeiro número do intervalo: '))
# ultimo = int(input('Digite o último número do intervalo: '))
# s = 0
# for num in range(primeiro, ultimo+1):
#     if num % 2 == 1 and num % 3 == 0:
#         s = s + num
# print(s)

#Crie um programa que mostre todos os números pares que estão no intervalo entre 1 e 50.

#resolução
print('-='*17)
print('NÚMEROS PARES ENTRE UM INTERVALO')
print('-='*17)
inicio = int(input('Digite o primeiro número do intervalo: '))
fim = int(input('Digite o último número do intervalo: '))
for c in range(inicio, fim+1):
    if c % 2 == 0:
        print('{}'.format(c),end=' ')


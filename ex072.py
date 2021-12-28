'''Crie um programa que tenha uma tupla totalmente preenchida com um contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 
        'Nove','Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
         'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {lista[num]}')
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar == 'S':
            continue
        elif continuar == 'N':
            break
        while continuar not in 'SN':
            print('Opção inválida.', end=' ')
            continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar == 'N':
            break
    else:
        print('Número inválido.',end=' ')
print('FIM')

#outra opção
'''while True:
    num = int(input('Digite um número entre 0 a 10: '))
    if num < 0 or num > 20:
        print('Número inválido.', end=' ')
    else:
        print(f'O número digitado foi {lista[num]}')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if resposta == 'N':
        break
print('FIM')'''

#outra opção
'''while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0:
        print('Número inválido.',end=' ')
        continue
    else:
        break
num_escolhido = lista[num]
print(f'Você digitou o número "{num_escolhido}"')'''

#outra opção
'''num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    print('Número inválido. Digite um número entre 0 e 20: ')   
    num = int(input('Digite um número entre 0 e 20: '))
num_escolhido = lista[num]
print(f'Você digitou o número "{num_escolhido}"')'''
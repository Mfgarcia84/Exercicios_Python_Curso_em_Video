'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores'''

#solução da aula
cont = soma = 0
resposta = 'S'
while resposta in 'S':
    num = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + num
    resposta = str(input('Deseja digitar outro número? [S/N]')).replace(' ','').upper()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('A média dos números digitados é {:.2f}'.format(media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))




#minha solução
'''s = 0
c = 0
encerrar = False
while not encerrar:
    num = int(input('Digite um número: '))
    c = c + 1
    s = s + num
    if c == 1:
        maior = num
        menor = num
    elif c > 1:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    novo_num = str(input('Deseja digitar mais números? [S/N] '))
    if novo_num == 'S':
        encerrar = False
    elif novo_num == 'N':
        encerrar = True
    else:
        sair = False
        while not sair:
            print('Opção inválida.')
            novo_num = str(input('Deseja digitar mais números? [S/N] '))
            if novo_num not in 'SN':
                sair = False
            else:
                sair = True
media = s / c
print('~'*50)
print('A média dos {} números digitados é {:.2f}'.format(c, media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
print('~'*50)'''




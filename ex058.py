'''Melhore o jogo do desafio ex028 aonde o computador vai pensar em um número entre 1 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''


from random import randint
computador = randint(1, 10)
print('Acabei de pensar em um número entre 1 e 10. Você consegue adivinhar qual foi?')
acertou = False
c = 0
while not acertou:
    jogador = int(input('Digite um número:  '))
    if jogador < 1 or jogador > 10:
        print('Número inválido. Digite um valor entre 1 e 10.')
    else:
        if jogador < computador:
            print('O número que você escolheu é menor. Tente um número maior.')
        if jogador > computador:
            print('O número que você escolheu é maior. Tente um número menor.')
        if jogador == computador:
            acertou = True
        c = c + 1
print('Você acertou com {} tentativa(s) válida(s).'.format(c))




'''import random
choice_computer = random.randint(0, 10) #Retorna um inteiro aleatório entre 0 e 10
print(choice_computer)
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
acertou = False
cont = 0
while not acertou:
    choice_player = int(input('Qual seu palpite? '))
    cont = cont + 1
    if choice_player == choice_computer:
        print('Acertou!!')
        acertou = True
    else:
        if choice_player < choice_computer:
            print('Mais...tente mais uma vez.')
        elif choice_player > choice_computer:
            print('Menos...tente mais uma vez.')
print('Você precisou de {} tentativas para acertar.'.format(cont))'''


# choice_player = int(input('Qual seu palpite? '))
# cont = 0
# while choice_player != choice_computer:#se a condição for verdadeira o laço continua. Se for falsa ele para.
#     if choice_player < choice_computer:
#         print('Mais...tente mais uma vez.')
#     else:
#         print('Menos...tente mais uma vez.')
#     cont = cont + 1
#     choice_player = int(input('Qual seu palpite? '))
# print('Você acertou! O número escolhido pelo computador foi {}.'.format(choice_computer))
# print('Você precisou de {} tentativas para acertar o número.'.format(cont+1))

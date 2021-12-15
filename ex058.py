'''Melhore o jogo do desafio ex028 aonde o computador vai pensar em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

#minha solução
'''from random import randint
computador = randint(0, 10)
print('~'*77)
print('Eu pensei em um número entre 0 e 10. Você consegue adivinhar qual número foi?')
print('~'*77)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Digite um número: '))
    if jogador != computador:
        if jogador < 0 or jogador > 10:
            print('Opção inválida! Digite um número entre 1 e 10.')
        else:
            if jogador < computador:    
                print('O número que você escolheu é menor. Tente um número maior.')
            if jogador > computador:
                print('O número que você escolheu é maior. Tente um número menor.')
    if jogador == computador:
        acertou = True
    palpites = palpites + 1
print('~'*66)
print('Parabéns! Você escolheu o número {} e eu também escolhi o número {}.'.format(jogador, jogador))
print('Você precisou de {} tentativas para acertar.'.format(palpites))
print('~'*66)'''

#solução aula
from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos...tente mais uma vez.')
        if jogador < computador:
            print('Mais...tente mais uma vez.')   
print('Parabéns! Você acertou com {} tentativas.'.format(palpites))
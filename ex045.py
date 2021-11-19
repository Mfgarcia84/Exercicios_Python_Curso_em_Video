#Crie um programa que faça o computador jogar jokenpô (pedra, papel, tesoura) com você.
# import random
# user = str(input('Escolha pedra, papel ou tesoura: '))
# comp = random.choice(['pedra','papel','tesoura'])
# print('O computador escolheu {}.'.format(comp))
# if user == 'papel' and comp == 'pedra':
#     print('Você ganhou! Papel cobre pedra.')
# elif user == 'papel' and comp == 'tesoura':
#     print('Você perdeu! Tesoura corta papel')
# elif user == 'papel' and comp == 'papel':
#     print('Jogue novamente. Não houve vencedor.')
# elif user == 'pedra' and comp == 'papel':
#     print('Você perdeu! Papel cobre pedra.')
# elif user == 'pedra' and comp == 'tesoura':
#     print('Você ganhou! Pedra quebra tesoura.')
# elif user == 'pedra' and comp == 'pedra':
#     print('Jogue novamente. Não houve vencedor.')
# elif user == 'tesoura' and comp == 'papel':
#     print('Você ganhou!. Tesoura corta papel.')
# elif user == 'tesoura' and comp == 'pedra':
#     print('Você pedeu! Pedra quebra tesoura.')
# elif user == 'tesoura' and comp == 'tesoura':
#     print('Jogue novamente. Não houve vencedor')
import random
from time import sleep
print()
print('-='*15,'VAMOS JOGAR JOKENPÔ?','-='*15)
print('''Escolha pedra, papel ou tesoura:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opcao_user = int(input('Escolha a opção 1, 2 ou 3: '))
if opcao_user == 1:
    escolha_user = 'Pedra'
elif opcao_user == 2:
    escolha_user = 'Papel'
elif opcao_user == 3:
    escolha_user = 'Tesoura'
else:
    escolha_user = 'uma opção inválida'
opcao_comp = random.choice([1,2,3])
if opcao_comp == 1:
    escolha_comp = 'Pedra'
elif opcao_comp == 2:
    escolha_comp = 'Papel'
elif opcao_comp == 3:
    escolha_comp = 'Tesoura'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*20,'\nVocê escolheu {}.'.format(escolha_user))
print('O computador escolheu {}.\n'.format(escolha_comp),'-='*20,sep='')
if opcao_user == opcao_comp:
    print('Não houve vencedor. Tente novamente.')
elif opcao_user == 1 and opcao_comp == 2:
    print('Você perdeu. Papel cobre pedra.')
elif opcao_user == 1 and opcao_comp == 3:
    print('Voce ganhou. Pedra quebra tesoura.')
elif opcao_user == 2 and opcao_comp == 1:
    print('Você ganhou. Papel cobre pedra.')
elif opcao_user == 2 and opcao_comp == 3:
    print('Você perdeu. Tesoura corta papel.')
elif opcao_user == 3 and opcao_comp == 1:
    print('Você perdeu. Pedra quebra tesoura.')
elif opcao_user == 3 and opcao_comp == 2:
    print('Você ganhou. Tesoura corta papel.')
else:
    print('\033[1:31mOpção Inválida. Digite um número de 1 a 3.\033[m')
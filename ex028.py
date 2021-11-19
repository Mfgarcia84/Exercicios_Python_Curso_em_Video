#escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
#seq = randint (0,5) outra maneira do computador escolher um número aleatório entre 0 e 5
seq = [0,1,2,3,4,5] #lista de números de 0 a 5
num_comp = random.choice(seq) #retorna um elemento aleatório da lista não vazia
#print(num_comp)
num_user = int(input('Digite um número entre 0 e 5: '))
print('Processando.....')
    sleep(2) #aguarda 2 segundos até mostrar na console a próxima linha do código
if num_user == num_comp:
    print('Você venceu! O número sorteado também foi {}.'.format(num_comp))
else:
    print('Você perdeu! O número sorteado foi {}.'.format(num_comp))





#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import emoji
import time
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print('-='*5,'FELIZ ANO NOVO','-='*5)
print(emoji.emojize(':stuck_out_tongue_closed_eyes:'*20,use_aliases=True))


# import emoji
# from time import sleep
# print('INICIANDO CONTAGEM REGRESSIVA PARA REVEILLON....')
# for c in range(10, 0, -1):
#     sleep(1)
#     print(c)
# sleep(1)
# print('-='*18)
# print(emoji.emojize(':tada:'*6, use_aliases=True), 'FELIZ 2022!!!', emoji.emojize(':tada:'*6, use_aliases=True))
# print('-='*18)




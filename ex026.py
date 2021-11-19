#crie um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "A".
#em que posição ela aparece a primeira vez.
#em que posição ela aparece a última vez.

import unidecode
frase = str(input('Digite uma frase: '))
frase_formatada = unidecode.unidecode(frase.strip().upper()) #retira os espaços do início e fim, transforma para maiúsculo e retira os acentos
print('A letra "A" aparece {} vezes.'.format(frase_formatada.count('A')))
print('A letra "A" aparece a primeira vez na posição {}.'.format(frase_formatada.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase_formatada.rfind('A')+1))

# import unidecode
# nome = input('Digite uma frase: ')
# print(unidecode.unidecode(nome)) retirar acentos das palavras




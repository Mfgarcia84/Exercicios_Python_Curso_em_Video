#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando todos os espaços.
#palíndromo: palavra ou frase que tem a mesma sequência de letras em qualquer ordem de leitura. Ex: Ovo


import unidecode
frase = unidecode.unidecode(str(input('Digite uma frase: '))).replace(' ','').upper()
inv_frase = frase[::-1]
print('A frase digitada foi: {}.'.format(frase))
print('A frase invertida é: {}.'.format(inv_frase))
if frase == inv_frase:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')


# import unidecode
# frase = unidecode.unidecode(str(input('Digite uma frase: ')).replace(' ','').upper())
# for c in frase [len(frase):0:-1]:
#     print(c,end='')

# for c in range((len(frase)), 0, -1):
#     print(c, end='')

















# import unidecode
# frase = unidecode.unidecode(str(input('Digite uma frase: ')).replace(' ','').upper())
# frase_invertida = frase[::-1]
# for c in frase_invertida()

#forma de fazer sem utilizar estrutura de laço for.
# import unidecode
# frase = unidecode.unidecode(str(input('Digite uma frase: ')).replace(' ','').upper())
# frase_invertida = frase[::-1]
# print(frase)
# print(frase_invertida)
# if frase == frase_invertida:
#     print('A frase é um palíndromo.')
# else:
#     print('A frase não é um palíndromo.')


# import unidecode
# frase = unidecode.unidecode(str(input('Digite uma frase: ')).replace(' ','').upper())
# #print(frase)
#
# for c in range(len(frase)-1, -1, -1):
#     inverso = frase[::-1]
#     print(inverso)





'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.

Ex.
Escreve('Olá, mundo!')

Saída.
~~~~~~~~~~~
Olá, mundo!
~~~~~~~~~~~
'''

def escreva(texto):
    print('~' * (len(texto)+4))
    print(f'  {texto}')
    print('~' * (len(texto)+4))


#Programa principal
while True:
    texto = str(input('Digite o texto: '))
    escreva(texto)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resposta == 'N':
        break



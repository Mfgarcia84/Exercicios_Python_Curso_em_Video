'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno com dimesões {largura} x {comprimento} é {area}m.')


#PROGRAMA PRINCIPAL
print('=' * 20)
print('CONTROLE DE TERRENO')
print('=' * 20)
largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento(m): '))
dimensao = area(largura, comprimento)



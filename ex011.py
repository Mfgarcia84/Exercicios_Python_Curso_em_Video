#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo qua cada litro de tinta pinta uma área de 2m2.
print()
print('='*50,'DESAFIO 011','='*50)
largura = float(input('Digite a largura em metros (m): '))
altura = float(input('Digite a altura em metros (m): '))
area = largura * altura
qtd_tinta = area/2
print('São necessários {:.1f} litros de tinta para pintar a parede.'.format(qtd_tinta))



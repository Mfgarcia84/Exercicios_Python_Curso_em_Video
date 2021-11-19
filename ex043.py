#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
#com a tabela abaixo:
#Abaixo de 18.5: abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: sobrepeso
#30 até 40: obesidade
#acima de 40: obseidade mórbida

peso = float(input('Digite o peso: (kg) '))
altura = float(input('Digite a altura: (m) '))
IMC = peso / (altura**2)
print('O IMC dessa pessoa é {:.1f}:'.format(IMC), end=' ')
if IMC < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= IMC < 25:
    print('Peso ideal.')
elif 25 <= IMC < 30:
    print('Sobrepeso.')
elif 30 <= IMC < 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')


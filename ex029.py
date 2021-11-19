#escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo
# que foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

vel_carro = float(input('Velocidade do carro: '))
vel_permitida = 80
if vel_carro > vel_permitida:
    print('Você foi multado por estar acima da velocidade permitida.')
    print('O valor da multa é: R${}'.format((vel_carro-vel_permitida)*7))
else:
    print('Você está dentro da velocidade permitida.')

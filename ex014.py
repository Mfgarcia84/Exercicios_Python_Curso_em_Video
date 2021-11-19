#Escreva um programa que converta uma temperatura digitada em Celsius e converta para Fahrenheit
print()
print('='*50,'DESAFIO 014','='*50)
temp = float(input('Digite a temperatura em graus celsius:(ºC) '))
f = temp * 1.8 + 32
print('A temperatura de {}ºC corresponde a {:.1f}ºF.'.format(temp,f))




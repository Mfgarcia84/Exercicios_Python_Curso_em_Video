#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
#sen (a) = cateto oposto/hipotenusa
#cos (a) = cateto adjacente/hipotenusa
#tan (a) = cateto oposto/cateto adjacente

import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))#necessário transformar o angulo para graus radianos, pois a função seno espera esse formato
cos = math.cos(math.radians(ang))#necessário transformar o angulo para graus radianos, pois a função cosseno espera esse formato
tan = math.tan(math.radians(ang))#necessário transformar o angulo para graus radianos, pois a função tangente espera esse formato
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(ang,sen,cos,tan))


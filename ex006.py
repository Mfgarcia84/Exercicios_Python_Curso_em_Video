#crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e raiz quadrada
print()
print('='*50,'{}'.format('DESAFIO 006'),'='*50)
num = int(input('Digite um número: '))
dobro = 2*num
triplo = 3*num
raiz = num**0.5
#print('O dobro de {} é {}, o triplo é {} e a raiz é {:.3f}.'.format(num,dobro,triplo,raiz)) assim ou conforme a linha abaixo
print('\033[1:30:46mO dobro de {} é {}, o triplo é {} e a raiz é {:.2f}\033[m'.format(num,num*2,num*3,num**(1/2)))#solução apenas com uma variável

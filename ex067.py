'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.
num x 1 =
num x 2 =
num x 3 =
num x 4 = 
num x 5 =
num x 6 =
num x 7 =
num x 8 =
num x 9 =
num x 10 =
'''
#minha solução
'''while True:
    print('-='*20)
    num = int(input('Quer ver a tabuada de qual número? '))
    print('-='*20)
    if num < 0:
        break
    else:
        for c in range(1, 11):
            print(num,'x',f'{c}','=',f'{num * c}')
print('Programa "Tabuada" encerrado!')'''
    
#solução da aula
while True:
    print('-='*20)
    num = int(input('Quer ver a tabuada de qual número? '))
    print('-='*20)
    if num < 0:
        break
    for c in range(1, 11): 
        print(num,'x',f'{c}','=',f'{num * c}')
print('Programa "Tabuada" encerrado!')

#Refaça o desafio ex009, mostrando a tabuada de um número que o usuário escolher, só que agora
#utilizando um laço for.

num = int(input('Digite um número: '))
print('-='*15)
print('TABUADA')
print('-='*15)
for c in range(1, 10):
    print('{} x {} = {}'.format(num, c, num*c))


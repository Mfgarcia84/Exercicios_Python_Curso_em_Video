#Refaça o desafio ex035 dos triângulos, acrecestando o recurso de mostrar que tipo de triângulo será formado:
#equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
if a < b +c and b < a + c and c < a + b:
    print('Os lados formam um triângulo:', end=' ')
    if a == b == c:
        print('Equilátero')
    elif a == b or a == c or b ==c:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Os lados não formam um triângulo')

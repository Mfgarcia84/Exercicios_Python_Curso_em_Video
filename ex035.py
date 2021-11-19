#desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[1:31m-='*20,'\033[m')
print('\033[1:30:44mAnalisador de Triângulo\033[m')
print('\033[1:31m-='*20,'\033[m')
a = float(input('Digite a medida do lado a: '))
b = float(input('Digite a medida do lado b: '))
c = float(input('Digite a medida do lado c: '))

lado_a = abs(b-c) < a < b + c
lado_b = abs(a-c) < b < a + c
lado_c = abs(a-b) < c < a + b
# print(lado_a)
# print(lado_b)
# print(lado_c)

if lado_a & lado_b & lado_c == True:
    print('Os lados formam um triângulo.')
else:
    print('Os lados não formam um triângulo.')

#r1<r2+r3 and r2<r1+r3 and r3<r1+r2 outra regra para formação de triângulo

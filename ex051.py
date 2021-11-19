#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
#primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo_n = int(input('Até qual termo da PA você quer mostrar? '))
an = termo + razao * (termo_n - 1)
print('-='*17)
print('Os {} primeiros termos da PA são: '.format(termo_n))
print('-='*17)
for c in range(termo, an+1, razao):
    print(c)


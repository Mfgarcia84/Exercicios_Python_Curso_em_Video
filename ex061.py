'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA
usando o estrutura while'''

# an = termo + razao * (termo_n - 1)

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo_n = 1
print('Os dez primeiros termos da razão são:')
while termo_n <= 10:
    an = primeiro_termo + razao * (termo_n - 1)
    termo_n = termo_n + 1
    print(an, end=' ')

'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA
usando o estrutura while'''

# an = termo + razao * (termo_n - 1)

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
enesimo_termo = int(input('Digite o enésimo termo da PA: '))
c = 1
while c <= enesimo_termo:
    print('{} ->'.format(primeiro_termo),end=' ')
    primeiro_termo = primeiro_termo + razao
    c = c + 1
print('FIM',end=' ')


# print('Os {} primeiros termos da PA são:'.format(enesimo_termo))
# while c <= enesimo_termo:
#     valor_enesimo_termo = primeiro_termo + razao * (c - 1)
#     print(valor_enesimo_termo,'->',end=' ')
#     c = c + 1
# print('FIM')

# primeiro_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))
# termo_n = 1
# print('Os dez primeiros termos da razão são:')
# while termo_n <= 10:
#     an = primeiro_termo + razao * (termo_n - 1)
#     termo_n = termo_n + 1
#     print(an, end=' ')

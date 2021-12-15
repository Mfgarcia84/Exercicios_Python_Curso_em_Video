'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA
usando o estrutura while'''

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
enesimo_termo = int(input('Digite o enésimo termo da PA: '))
print('O {} primeiros termos da PA são:'.format(enesimo_termo))
c = 1
while c <= enesimo_termo:
    print(primeiro_termo, end=' ')
    primeiro_termo = primeiro_termo + razao
    c = c + 1


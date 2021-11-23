'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos'''
#an = termo + razao * (termo_n - 1)

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
enesimo_termo = int(input('Até qual termo da razão você deseja mostrar? '))
while enesimo_termo != 0:
    cont = 1
    while cont <= enesimo_termo:
        print('{}->'.format(primeiro_termo),end=' ')
        primeiro_termo = primeiro_termo + razao
        cont = cont + 1
    print('PAUSA')
    enesimo_termo = int(input('Deseja mostrar mais quantos termos? '))
print('FIM')









# primeiro_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))
# enesimo_termo = int(input('Informe até qual termo deseja ver: '))
# while enesimo_termo != 0:
#     c = 1
#     while c <= enesimo_termo:
#         print('{} ->'.format(primeiro_termo),end=' ')
#         primeiro_termo = primeiro_termo + razao
#         c = c + 1
#     print('PAUSA...')
#     enesimo_termo = int(input('Deseja mostrar mais quantos termos? '))
# print('FIM')

















'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos'''

#an = termo + razao * (termo_n - 1)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
enesimo_termo = int(input('Informe o enésimo termo: '))
print('Os {} primeiros termos da PA são:'.format(enesimo_termo))
termo = 1
while termo <= enesimo_termo:
    an = primeiro_termo + razao * (termo - 1)
    print(an,end=' ')
    termo = termo + 1

# print('\nQuer mostrar mais termos? \n[0] não\n[1] sim')
# opcao = int(input('Digite uma das opções: '))
# while opcao == 1:
#     enesimo_termo = int(input('Deseja mostrar mais quantos termos? '))



# if opcao == 0:
#     print('FIM')
# if opcao == 1:
#     enesimo_termo = int(input('Deseja mostrar mais quantos termos? '))
#     termo = 1
#     while termo <= enesimo_termo:
#         ax = (an+razao) + razao * (termo - 1)
#         termo = termo + 1
#         print(ax,end=' ')



    # if c > enesimo_termo:
    #     print('\nQuer mostrar mais termos?\n[0] não\n[1] sim')
    #     opcao = int(input('Digite uma das opções: '))
    #     if opcao == 0:
    #         print('FIM')
    #     if opcao == 1:
    #         enesimo_termo = int(input('Deseja mostrar mais quantos termos? '))
    #         c = 1
    #         while c <= enesimo_termo:
    #             ax = (an+razao) + razao * (c - 1)
    #             print(ax,end=' ')
    #             c = c + 1
    #             print(an)








# primeiro_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))
# termo_n = 1
# print('Os dez primeiros termos da razão são:',end=' ')
# while 0 < termo_n <= 10:
#     an = primeiro_termo + razao * (termo_n - 1)
#     termo_n = termo_n + 1
#     print(an, end=' ')
#     if termo_n > 10:
#         termo_n = int(input('\nDeseja mostrar mais quantos termos? '))
#         if termo_n == 0:
#             print('FIM')
#         while termo_n > 0:
#             ax = an + razao * (termo_n - 1)
#             termo_n = termo_n - 1
#             print(ax,end=' ')

# primeiro_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))
# termo_n = 1
# print('Os dez primeiros termos da razão são:',end=' ')
# while 0 < termo_n <= 10:
#     an = primeiro_termo + razao * (termo_n - 1)
#     termo_n = termo_n + 1
#     print(an, end=' ')
# novos_termos = int(input('\nDeseja mostrar mais quantos termos? '))



# if novos_termos == 0:
#     print('FIM')
# else:
#     termo_n = 1
#     while 0 < termo_n <= novos_termos:
#         ax = (an+razao) + razao * (termo_n - 1)
#         termo_n = termo_n + 1
#         print(ax,end=' ')
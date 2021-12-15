'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos'''

#minha solução
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
enesimo_termo = int(input('Digite o enésimo termo da PA: '))
print('O {} primeiros termos da PA são:'.format(enesimo_termo))
encerrar = False
termos = 0
while not encerrar:
    c = enesimo_termo
    while c >= 1:
        print(primeiro_termo, '-->', end=' ')
        primeiro_termo = primeiro_termo + razao
        c = c - 1
        termos = termos + 1
    print('PAUSA')
    enesimo_termo = int(input('\nDeseja mostrar mais quantos termos? '))
    if enesimo_termo > 0:
        encerrar = False
    if enesimo_termo == 0:
        encerrar = True
print('Progressão finalizada com {} termos.'.format(termos))
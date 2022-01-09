'''
Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno indivudualmente.
'''


dados_total = []
dados_aluno = []
while True:
    dados_aluno.append(str(input('Nome: ')))
    dados_aluno.append(float(input('Nota 1: ')))
    dados_aluno.append(float(input('Nota 2: ')))
    dados_aluno.append((dados_aluno[1] + dados_aluno[2]) / 2)
    dados_total.append(dados_aluno[:])
    dados_aluno.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resposta == 'N':
        break
print('-='*40)
print(dados_total)


print(f'{"N°":<5}', f'{"NOME":<10}', f'{"MÉDIA":>5}')
print('-'*30)

for x,y in enumerate(dados_total):
    print(f'{x:<5}', f'{y[0]:<10}', f'{y[3]:>5}')


'''for l in range(len(dados_total)):
    for c in range(4):
        if c == 0:
            print(f'{l:<5}', f'{dados_total[l][0]:<10}', end=' ')
        elif c == 3:
            print(f'{dados_total[l][3]:>5}')
print('-' * 30)'''



while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    else:
        for l in range(len(dados_total)):
            if mostrar == l:
                print(f'Notas de {dados_total[l][0]} são: {dados_total[l][1]} e', f'{dados_total[l][2]}')
print('\nFIM DO PROGRAMA')
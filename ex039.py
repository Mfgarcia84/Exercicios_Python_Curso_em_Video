#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar:
#Se é hora de se alistar:
#Se já passou do tempo de alistamento:
#O programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
nascimento = int(input('Digite o ano de nascimento: '))
print('Informe o sexo:\n[1]-M\n[2]-F')
sexo = int(input('Digite a opção 1 ou 2: '))
data = datetime.date.today().year #informa o ano atual
idade = data - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento,idade,data))
if sexo == 2:
    print('Você é do sexo feminino, não precisa de alistar.')
elif idade < 18:
    print('Ainda irá se alistar.')
    print('Falta {} anos para o alistamento.'.format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    print('Já passou o tempo de alistamento.')
    print('Passaram {} anos do prazo de alistamento.'.format(idade-18))







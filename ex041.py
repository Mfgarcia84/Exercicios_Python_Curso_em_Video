#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com sua idade:
#até 9 anos: Mirim
#até 14 anos: Infantil
#até 19 anos: Junior
#até 25 anos: Senior
#acima: master
import datetime

ano = int(input('Digite o ano de nascimento: '))
idade = datetime.date.today().year - ano
print(idade)
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 25:
    print('Senior')
else:
    print('Master')

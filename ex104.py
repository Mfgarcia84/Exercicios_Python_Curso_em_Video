'''
Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante
à função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n')
'''

'''#minha solução
def leiaInt(texto):
    while True:
        num = input(texto)
        if num.isnumeric():
            return int(num)
            break
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''



#solução aula
def leiaInt(texto):
    valor = 0
    ok = False
    while True:
        num = str(input(texto))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
'''
Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de calculo de fatorial.
'''

'''def fatorial(num, show=0):
    from time import sleep
    fat = 1
    for i in range(num, 0, -1):
        if show == 0:
            fat = fat * i
        if show == 1:
            print(f'{i} x' if i > 1 else i, end=' ')
            fat = fat * i
            sleep(0.5)
    print(f'\nO fatorial de {num} é: {fat}')

#Programa principal
num = int(input('Número: '))
show = int(input('Mostrar cálculo? (1-SIM / 0-NÃO) '))
fatorial(num, show)'''

def fatorial(num, show=False):
    """
    --> Calcula o fatorial de um número
    :param num: O número que será calculado o fatorial
    :param show: Mostra o processo de cálculo
    :return: O valor do fatorial do número
    """
    from time import sleep
    fat = 1
    for i in range(num, 0, -1):
        fat = fat * i
        if show:
            print(f'{i} x' if i > 1 else i, end=' ')
            sleep(0.5)
    return f'\nO fatorial de {num} é: {fat}'

#Programa principal
resultado = fatorial(4,True) #Pode ser True ou False
print(resultado)


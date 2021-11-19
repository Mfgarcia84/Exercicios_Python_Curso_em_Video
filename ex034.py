#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o salário: R$ '))
if salario > 1250:
    print('O salário reajustado com 10% é R${:.2f}.'.format(salario+salario*0.10))
else:
    print('O salário reajustado com 15% é R${:.2f}.'.format(salario+salario*0.15))


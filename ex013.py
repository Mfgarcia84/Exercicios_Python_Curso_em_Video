#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
print()
print('='*50,'DESAFIO 013','='*50)
salario = float(input('Digite o salário atual (R$): '))
salario_ajustado = salario + salario*0.15
print('O salário reajustado é R$ {:.2f}'.format(salario_ajustado))
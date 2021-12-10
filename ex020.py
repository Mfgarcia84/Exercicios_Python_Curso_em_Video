#Um prefessor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
from random import shuffle #importando apenas o método shuffle do módulo random
print()
print('='*25,'DESAFIO 020','='*25)
a1 =  str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do alune 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista) #embaralha a lista antes de ser mostrada na console
print('\nA ordem de apresentação será:\n',lista)










'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
- quantidade de notas
- a maior nota
- a menor nota
- a média da turma
- a situção (opcional)
adicione também as docstrings na função
'''

def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações dos alunos
    :param n: notas
    :param sit: situação
    :return: dicionário com várias informações
    """
    dic = {}
    dic['qtde_notas'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    med = sum(n) / len(n)
    dic['média'] = med
    if sit:
        if med >= 7:
            dic['situação'] = 'boa'
        elif 5 <= med < 7:
            dic['situação'] = 'razoável'
        else:
            dic['situação'] = 'ruim'
    return dic

#Programa principal
resp = notas(5.5, 9.5, 1.5, sit=True)
print(resp)

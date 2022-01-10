# TUPLAS
"""lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #tupla começa com '()'
lista_ordenada = sorted(lanche) #ordena a lista (nesse caso em ordem alfabética)
print(lanche)
print(lista_ordenada)"""

"""a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # + em tupla faz a concatenação criando uma tupla nova 'c'
d = b + a # a ordem altera os fatores aqui
print(c)
print(d)"""

"""a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b 
print(c.count(5)) #conta quantas vezes aparece o numero 5 na tupla c"""

"""a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8)) # em que posição está o número 8 na tupla c (retorna a posição da primeira aparição)?"""

# LISTAS
"""numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
objetos = ('Monitor', 'Laptop', 'Computador', 'Mouse')"""


"""comidas = ('Refrigerante', 'Macarronada', 'Pizza', 'Bolo', 'Suco')
pares = enumerate(comidas) #enumera a lista
print(next(pares))# printa a enumeração: (indice, objeto da lista) ex: (0, 'Refrigerante')
print(next(pares))# printa a enumeração: (indice, objeto da lista) ex: (1, 'Macarronada')
print(next(pares))# printa a enumeração: (indice, objeto da lista) ex: (2, 'Pizza')
print(next(pares))# printa a enumeração: (indice, objeto da lista) ex: (3, 'Bolo')
print(next(pares))# printa a enumeração: (indice, objeto da lista) ex: (4, 'Suco')
print(list(pares))"""

# unpacking

'''par = (0, 'Marcelo') #tupla com dois elementos
posicao = par[0] #quebra a tupla 'par' em duas variáveis (posicao e nome)
nome = par[1] #quebra a tupla 'par' em duas variáveis (posicao e nome)
print(posicao, nome)'''

'''posicao, nome = par # mesma resultado do código acima. A posicao recebe o objeto do indice 0 de par e nome recebe o objeto do indice 1 de par
print(posicao, nome)"""

"""comidas = ('Refrigerante', 'Macarronada', 'Suco', 'Bolo')
print(comidas)
var = enumerate(comidas, start=1) #gera tuplas enumeradas dentro de listas
lista = list(var)
print(lista)
for a, b in enumerate(comidas, start=1):
    print(f'#{a} - {b}')"""
""" enumerate retorna os objetos da tupla/lista com seu respectivo índice (nesse caso caso começando em 1 e não 0)
    (1, 'Refrigerante')
    (2, 'Macarronada')
    (3, 'Suco')
    (4, 'Bolo')
    

    Na primeira passagem do for pela lista:
    a variável "a" recebe 1 e "b" recebe Refrigerante
    output da primeira passagem: #1 - Refrigerante

    Na segund passagem do for pela lista:
    a variável "a" recebe 2 e "b" recebe Macarronada
    output da primeira passagem: #2 - Macarronada

    E assim por diante até a última volta do FOR
"""


# cont. Listas compostas

"""teste = list()
teste.append("Gustavo")
teste.append(40)
print(teste)
galera = list()
galera.append(
    teste[:]
)  # faz uma interligação entre as listas. Se mudar a primeira lista teste, automaticamente muda a segunda lista galera
print(galera)
teste[0] = "Maria"
teste[1] = 22
print(galera)
galera.append(teste[:])
print(galera)"""

''''''galera = list()
dado = list()
for c in range(3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])  # cópia de dado
    dado.clear()
print(galera)'''

'''for p in galera:
    if p[1] > 35:
        print(f"{p[0]} tem mais de 35 anos.")
    else:
        print(f"{p[0]} tem menos de 35 anos.")''''''


''''''galera = [["marcelo", 37], ["thamiris", 34], ["renato", 35]]
for p in range(3):
    print(f"{galera[p][0]} tem anos {galera[p][1]} de idade.")''''''

print('casa')
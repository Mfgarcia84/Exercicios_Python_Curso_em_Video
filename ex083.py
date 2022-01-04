"""Crie um programa onde um usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parêntese abertos
e fechados na ordem correta.
"""

expressao = str(input("Digite uma expressão: "))
lista = []
for simb in expressao:
    if simb == "(":
        lista.append("(")
    elif simb == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
print(lista)
if len(lista) == 0:
    print("Expressão válida")
else:
    print("Expressão inválida")

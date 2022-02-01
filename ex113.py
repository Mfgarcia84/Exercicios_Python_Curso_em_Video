''''
113. Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade de digitação
de um número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.
'''


#definição da função
def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
            return i
            break
        except ValueError:
            print("\033[0;31mErro. Por favor digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print("O usuário preferiu não digitar esse número")
            i = 0
            return i
            break

def leiafloat(msg):
    while True:
        try:
            r = float(input(msg))
            return r
            break
        except ValueError:
            print("\033[0;31mErro. Por favor digite um número real válido.\033[m")
        except KeyboardInterrupt:
            print("O usuário preferiu não digitar esse número")
            r = 0
            return r
            break


#programa principal - validação de dados com tratamento de exceção
i = leiaint("Digite um número inteiro: ")
r = leiafloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {i} e o real foi {r}")



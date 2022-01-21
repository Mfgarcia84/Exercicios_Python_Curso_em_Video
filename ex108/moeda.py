def aumentar(preco=0, porcentagem=0):
    resultado = (preco * porcentagem/100) + preco
    return resultado

def reduzir(preco=0, porcentagem=0):
    resultado = preco - (preco * porcentagem/100)
    return resultado

def dobro(preco=0):
    resultado = preco * 2
    return resultado

def metade(preco=0):
    resultado = preco / 2
    return resultado

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',') #atentar para o retorno não tem o print




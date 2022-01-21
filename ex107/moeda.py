def aumentar(preco, porcentagem):
    resultado = (preco * porcentagem/100) + preco
    return resultado

def reduzir(preco, porcentagem):
    resultado = preco - (preco * porcentagem/100)
    return resultado

def dobro(preco):
    resultado = preco * 2
    return resultado

def metade(preco):
    resultado = preco / 2
    return resultado




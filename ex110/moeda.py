def aumentar(preco=0, porcentagem=0, formatar=False):
    """

    :param preco:
    :param porcentagem:
    :param formatar:
    :return:
    """
    resultado = (preco * porcentagem/100) + preco
    if formatar:
        return moeda(resultado)
    else:
        return resultado

def reduzir(preco=0, porcentagem=0, formatar=False):
    resultado = preco - (preco * porcentagem/100)
    if formatar:
        return moeda(resultado)
    else:
        return resultado

def dobro(preco=0, formatar=False):
    resultado = preco * 2
    if formatar:
        return moeda(resultado)
    else:
        return resultado


def metade(preco=0, formatar=False):
    resultado = preco / 2
    if formatar:
        return moeda(resultado)
    else:
        return resultado


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',') #atentar para o retorno não tem o print


def resumo(preco, aumento, reducao):
    print('=='*15)
    print('RESUMO DO VALOR'.center(30))
    print('=='*15)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, formatar=True)}')
    print(f'Metade do preço: \t{metade(preco, formatar=True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, formatar=True)}')
    print(f'{reducao}% de redução: \t{reduzir(preco, reducao, formatar=True)}')
    print('==' * 15)

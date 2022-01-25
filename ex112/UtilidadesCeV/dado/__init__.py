def leiadinheiro(msg):
    while True:
        entrada = input(msg).replace(',','.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'\033[0;31mErro: "{entrada}" não é um número válido!\033[m')
        else:
            entrada = float(entrada)
            break
    return entrada



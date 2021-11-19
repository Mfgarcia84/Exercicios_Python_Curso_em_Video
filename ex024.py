#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip().upper()
if cidade[0:5] == 'SANTO':
    print('A cidade começa com "SANTO"')
else:
    print('A cidade não começa com "SANTO"')


















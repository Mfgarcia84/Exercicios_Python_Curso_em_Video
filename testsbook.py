'''def greet_user(username): #username na definição da função é um parâmetro
    # (dado necessário para a função executar o código).
    print(f'Hello, {username}!')


#programa principal
greet_user('Marcelo') #'Marcelo' na chamada da função é um argumento (é uma informação passada na chamada da função).
#o argumento é armazendo no parâmetro'''


'''def describe_pet(animal_type, pet_name):
    print(f'Eu tenho um {animal_type} e ele se chama {pet_name}.')

describe_pet('cachorro', 'Bob)'''



'''def get_formatted_name(firstname, lastname, middlename=''): #python intrepreta strings vazias como False
    if middlename:
        fullname = firstname + ' ' + middlename + ' ' + lastname
    else:
        fullname = firstname + ' ' + lastname

    return fullname.title()

musico = get_formatted_name('marcelo', 'garcia', 'figueiredo')
print(musico)'''



'''def formatted_name(firstname, lastname, middlename=''):
    if middlename:
        fullname = (firstname + ' ' + middlename + ' ' + lastname).title()

    else:
        fullname = (firstname + ' ' + lastname).title()

    return fullname


jogador = formatted_name('marcelo', 'garcia', 'figueiredo')
print(jogador)
'''


'''def build_person(first_name, last_name, age=''):
    if age:
        person = {'first':first_name, 'last':last_name, 'age':age}
    else:
        person = {'first':first_name, 'last':last_name}

    return person #retornando uma lista para a chamada da função

musician = build_person('Jimi', 'Handrix', 29)
print(musician)'''



'''def get_formatted_name(first_name, last_name):
    fullname = first_name + ' ' + last_name
    return fullname.title()

#CÓDIGO PRINCIPAL
while True:
    print('Please tell me your name: (enter "q" at any time to quit).' )
    f_name = input('First_name: ')
    if f_name == 'q':
        break
    l_name = input('Last_name: ')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f'Hello, {formatted_name}!')'''

#NOMES DE CIDADE
'''def city_country(city, country):
    cc = '"' + city + ',' + ' ' + country + '"'
    return cc.title()


for i in range(3):
    city_name = str(input('City Name: '))
    country_name = str(input('Country Name: '))
    func_city_country = city_country(city_name, country_name)
    print(func_city_country)'''

#8.7 ALBUM
'''def make_album(artist_name, album_title, track_numbers=''):
    if track_numbers:
        album = {'artist_name':artist_name, 'album_title':album_title, 'track_numbers':track_numbers}
    else:
        album = {'artist_name': artist_name, 'album_title': album_title}
    return album

colecao = make_album('marcelo', 'qualquerum',6)
print(colecao)'''

#8.8 ALBUM DOS USUARIOS
'''def make_album(artist_name, album_title, track_numbers=''):
    if track_numbers:
        album = {'artist_name':artist_name, 'album_title':album_title, 'track_numbers':track_numbers}
    else:
        album = {'artist_name': artist_name, 'album_title': album_title}
    return album

while True:
    art_name = str(input('Nome (enter "q" to exit): '))
    if art_name == 'q':
        break
    alb_name = str(input('Album (enter "q" to exit): '))
    if art_name == 'q':
        break

    colecao = make_album(art_name, alb_name)
    print(colecao)
'''

'''def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)'''



'''unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)'''

'''
def func1(arg1):
    while arg1:
        current_design = arg1.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def func2(arg1):
    print("\nThe following models have been printed:")
    for i in completed_models:
        print(i)

#PROGRAMA PRINCIPAL
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
func1(unprinted_designs)
func2(completed_models)
'''



'''def func1(arg1):
    while arg1:
        current_design = arg1.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def func2(arg1):
    print("\nThe following models have been printed:")
    for i in completed_models:
        print(i)

#PROGRAMA PRINCIPAL
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
func1(unprinted_designs[:]) #vai enviar para a função uma cópia da lista original
func2(completed_models)
print(f'\nLista original: {unprinted_designs}')'''

#8.9 - MÁGICOS

'''def mostre_magicos(nome_magicos):
    for magico in nome_magicos:
        print(magico)


nome_magicos = ['marcelo', 'renato', 'lainho', 'velho boy']
print('Os mágicos são: ')
mostre_magicos(nome_magicos)'''


#8.10 – Grandes mágicos

'''def mostre_magicos(nome_magicos):
    for magico in nome_magicos:
        print(magico, end=' ')

def make_great(nome_magicos):
    for i in range(len(nome_magicos)):
        nome_magicos[i] = 'O grande' + ' ' + nome_magicos[i]
    print(nome_magicos)


nome_magicos = ['marcelo', 'renato', 'lainho', 'velho boy']
print('Lista original: ')
mostre_magicos(nome_magicos)
print('\nLista modificada: ')
make_great(nome_magicos)
'''

'''#8.11 – Mágicos inalterados

def mostre_magicos(nome_magicos):
    for magico in nome_magicos:
        print(magico)

def make_great(nome_magicos):
    for i in range(len(nome_magicos)):
        nome_magicos[i] = 'O grande' + ' ' + nome_magicos[i]
    print(nome_magicos)


nome_magicos = ['marcelo', 'renato', 'lainho', 'velho boy']
print(nome_magicos)
mostre_magicos(nome_magicos)

make_great(nome_magicos)'''

'''def make_pizza(*pizza): #agrupa/encapsula vários argumentos informados na chamada da função em uma tupla
    for ingrediente in pizza:
        print(f'- {ingrediente}')

make_pizza('tomate', 'cebola', 'orégano', 'queijo')'''



'''def make_pizza(a, b, **n): # asterisco cria tupla
    print(a)
    print(b)
    print(c)


make_pizza('tomate', 'cebola', 'queijo', 'orégano', 'presunto')'''





'''def build_profile(first, last, **user_info): # asteriscos fazem Python criar um dicionário vazio chamado user_info e colocar quaisquer pares nome-valor recebidos nesse dicionário
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile

profile = {}
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)'''


#8.12 – Sanduíches

'''def fazer_sanduiche(sanduiche):
    print('Itens do sanduiche:')
    for item in sanduiche:
        print(f'- {item}')


itens_sanduiche = ['cebola', 'tomate', 'alface', 'bacon', 'calabresa', 'batata', 'couve', 'carne']
fazer_sanduiche(itens_sanduiche)'''

'''from time import sleep

def contador(i, f, p): #para criar uma docstring da função insere aspas logo abaixo da definição
    """
    --> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    for i in range(i, f+1, p):
        print(i, end=' ')
        sleep(0.5)


contador(10, 100, 10)
help(contador)'''

#escopo de variáveis local e global
'''def fun():
    global n1 
    n1 = 4
    print(f'n1 dentro vale {n1}')

n1 = 2
fun()
print(f'n1 fora vale {n1}')'''

'''def fatorial(num=1):
    n = num - 1
    fat = num
    while n > 0:
        fat = fat * n
        n = n - 1
    print(f'fatorial de {num} é {fat}')


fatorial(5)'''

'''from datetime import date
a = date.today().year
print(a)'''

'''teste = int(input('Mostrar? '))
if teste == 1:
    teste = True
elif teste == 0:
    teste = False
print(teste)'''

n = 2
n.
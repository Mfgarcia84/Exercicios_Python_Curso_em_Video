n = input('Digite algo: ')
print('Tipo primitivo: {}'.format(type(n)))
print('É decimal? {}{}{}'.format('\033[1:31m',n.isdecimal(),'\033[m'))
print('Está em minúscula? {}{}{}'.format('\033[1:31m',n.islower(),'\033[m'))
print('Está em maiúscula? {}{}{}'.format('\033[1:31m',n.isupper(),'\033[m'))
print('Está capitalizada? {}{}{}'.format('\033[1:32m',n.istitle(),'\033[m'))
print('É um caractere alfabético? {}{}{}'.format('\033[1:32m',n.isalpha(),'\033[m'))
print('É um número? {}{}{}'.format('\033[1:31m',n.isnumeric(),'\033[m'))
print('É somente espaços? {}{}{}'.format('\033[1:31m',n.isspace(),'\033[m'))



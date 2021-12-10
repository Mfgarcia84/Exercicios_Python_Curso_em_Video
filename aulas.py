# contador: c = c + 1, sendo c = 0
# somador: s = s + num, sendo s = 0 e num = algum resultado anterior

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n!= 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es).'.format(par, impar))




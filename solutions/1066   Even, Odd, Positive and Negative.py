impar = 0
par = 0
positivo = 0
negativo = 0

for i in range(0, 5, 1):

    num = int(input())

    if (num % 2 == 0):
        par = par + 1

    elif (num % 2 == 1):
        impar = impar + 1

    if (num > 0):
        positivo = positivo + 1

    elif (num < 0):
        negativo = negativo + 1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))

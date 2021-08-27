cont = 0
media = 0

while cont < 2:
    nota = float(input())

    if nota >= 0 and nota<=10:
        cont = cont + 1
        media = media + nota

    if nota < 0 or nota > 10:
        print("nota invalida")

media = media/2

print('media = {}'.format(media))
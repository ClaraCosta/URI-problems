soma = 0
media = 0

for i in range(0, 6, 1):

    num = float(input())

    if num > 0:
        soma = soma + num
        media = media + 1

print(media, 'valores positivos')
print('%.1f' % (soma / media))


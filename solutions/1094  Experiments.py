totCobaias = 0
totC = 0
totR = 0
totS = 0

N = int(input())

for i in range(1, N + 1):
    qtde, tipo = input().split()

    qtde, tipo = int(qtde), str(tipo)

    totCobaias = totCobaias + qtde

    if tipo == 'C':
        totC = totC + qtde

    if tipo == 'R':
        totR = totR + qtde

    if tipo == 'S':
        totS = totS + qtde

perCoe = (totC / totCobaias) * 100
perRat = (totR / totCobaias) * 100
perSap = (totS / totCobaias) * 100

print('Total: {} cobaias'.format(totCobaias))
print('Total de coelhos: {}'.format(totC))
print('Total de ratos: {}'.format(totR))
print('Total de sapos: {}'.format(totS))
print('Percentual de coelhos: {:.2f} %'.format(perCoe))
print('Percentual de ratos: {:.2f} %'.format(perRat))
print('Percentual de sapos: {:.2f} %'.format(perSap))


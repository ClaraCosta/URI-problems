maior = int(input())
posicao = 1

for i in range(1, 100):
    prox = int(input())

    if prox > maior:
        maior = prox
        posicao = i + 1

print(maior)
print(posicao)

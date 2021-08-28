N = int(input())
X = []
posicao = 0

num = list(map(int,input().split()))

for i in range(N):
    X.insert(i,num[i])
print('Menor valor: {}'.format(min(X)))

for i in range(N):
    if X[i]==min(X):
        posicao = i


print('Posicao: {}'.format(posicao))



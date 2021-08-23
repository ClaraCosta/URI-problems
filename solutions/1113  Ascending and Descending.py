n1, n2 = map(int, input().split())

while n1 != n2:

    if n1 > n2:
        print('Decrescente')

    elif n2 > n1:
        print('Crescente')

    elif n1 == n2:
        break

    n1, n2 = map(int, input().split())



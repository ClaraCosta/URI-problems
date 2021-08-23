R = 0
count = 0
N = int(input())

for i in range(1, 11, 1):
    count = i + 1
    R = i * N

    print("{} x {} = {}".format(i, N, R))


num = int(input())
rpm = []
rpm = input().split()
queda = 0

for i in range(1, num):

    if (int(rpm[i - 1]) > int(rpm[i])):
        queda = i + 1
        break

print(queda)
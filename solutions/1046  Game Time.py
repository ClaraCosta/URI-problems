I, T = input().split()
I = int(I)
T = int(T)

if I<T:
    Dur = T-I
else:
    Dur = (24-I)+T

print("O JOGO DUROU %d HORA(S)" %Dur)

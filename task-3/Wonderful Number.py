def binary_representation(N):
    y = bin(N)[2:]
    z = y[::-1]
    if y == z:
        print("YES")
    else:
        print("NO")

N = int(input())
if N % 2 == 0:
    print("NO")
else:
    binary_representation(N) 
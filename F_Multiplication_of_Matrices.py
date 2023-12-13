AR, AC = map(int, input().split())
A = [[0 for _ in range(AC)] for _ in range(AR)]
for i in range(AR):
    for j in range(AC):
        A[i][j] = int(input())

BR, BC = map(int, input().split())
B = [[0 for _ in range(BC)] for _ in range(BR)]
for i in range(BR):
    for j in range(BC):
        B[i][j] = int(input())

print(A)
print(B)

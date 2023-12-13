def swap_row(A, X, Y):
    A[X], A[Y] = A[Y], A[X]

def swap_column(A, X, Y, N):
    for i in range(N):
        A[i][X], A[i][Y] = A[i][Y], A[i][X]

def print_matrix(A):
    for row in range(len(A)):
        print(*A[row])

N, X, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

X -= 1
Y -= 1

swap_row(A, X, Y)
swap_column(A, X, Y, N)

print_matrix(A)

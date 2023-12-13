def is_subsequence(N, M, A, B):
    i, j = 0, 0
    
    while i < N and j < M:
        if A[i] == B[j]:
            j += 1
        i += 1
    
    return "yes" if j == M else "no"

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = is_subsequence(N, M, A, B)

print(result)

def permutation(N, A, B):

    return "yes" if sorted(A) == sorted(B) else "no"

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))  

result = permutation(N, A, B)
print(result)

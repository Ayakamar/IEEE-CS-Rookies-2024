def New_array(N, A, B):
    new = B + A
    return new


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = New_array(N, A, B)


print(*result)

def equation(X,N):
    s = 0
    for i in range(2, N+1,2):
        s= s + (X**i)
    return s    

X, N = map(int, input().split())

result = equation(X,N)
print(result)
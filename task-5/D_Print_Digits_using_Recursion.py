def digits(N):
    Number = []
    if N < 10:
        Number.append(N)
    else:
        Number.extend(digits(N // 10)) 
        remainder = N % 10
        Number.append(remainder)

    return Number

T = int(input( ))
for _ in range(T):
    N = int(input())
    result = digits(N)
    print(*result)

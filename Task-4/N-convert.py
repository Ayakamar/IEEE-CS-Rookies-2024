def convert_to_decimal(N, X):
    result = 0
    digit_list = [int(i) for i in str(N)]
    for i in range(len(digit_list)):
        result += digit_list[i] * (X ** i)
    return result

def convert_from_decimal(N, X):
    remeder=""
    while N > 0:
        remeder +=str(N % X)
        N = N // X  
    return   remeder[::-1]

T = int(input())
N, X = map(int, input().split())

if T == 1:
    result = convert_to_decimal(N, X)
    print(result)
elif T == 2:
    result = (convert_from_decimal(N, X))
    print(result)



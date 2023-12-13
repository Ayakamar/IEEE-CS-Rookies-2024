import math

def is_prime(num):
    if num == 1:
        return "NO"
    elif num == 2:
        return "YES"
    elif num % 2 == 0:
        return "NO"
    
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return "NO"
    
    return "YES"

T = int(input())
for _ in range(T):
    num = int(input())
    result = is_prime(num)
    print(result)

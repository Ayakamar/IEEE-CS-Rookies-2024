import math

def Greater_Common_Div(a, b):
    return math.gcd(a, b)

def Lowest_common_Mult(a, b):
    return a * b // (Greater_Common_Div(a, b))

A, B = map(int, input().split())
GCD = Greater_Common_Div(A, B)
LCM = Lowest_common_Mult(A, B)
result = [GCD, LCM]
print(*result)

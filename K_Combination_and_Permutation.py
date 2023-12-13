def factorial_range_product(start, end):
    result = 1
    for i in range(start, end , -1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

A, B = map(int, input().split())

M = factorial_recursive(A - B)
NIC = factorial_range_product(A, B) // M
NPC = factorial_recursive(A) // M

result = [NIC, NPC]
print(*result)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def number_of_divisors(n):
    divisors_count = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors_count += 2 if i != n // i else 1
    return divisors_count

n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
min_val = min(arr)
palindrome_counter = sum(1 for x in arr if is_palindrome(x))
prime_counter = sum(1 for x in arr if is_prime(x))

max_divisors_val = 0
answer = 0

for x in arr:
    divisors_count = number_of_divisors(x)
    if divisors_count == max_divisors_val:
        answer = max(answer, x)
    elif divisors_count > max_divisors_val:
        answer = x
        max_divisors_val = divisors_count

print("The maximum number :", max_val)
print("The minimum number :", min_val)
print("The number of prime numbers :", prime_counter)
print("The number of palindrome numbers :", palindrome_counter)
print("The number that has the maximum number of divisors :", answer)

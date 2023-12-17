def febonacci(n):
    if n ==1:
        return 0
    elif n==2:
        return 1
    elif n>=3:
        return febonacci(n-1) + febonacci(n-2)

n = int(input())
result = febonacci(n)
print(result)    
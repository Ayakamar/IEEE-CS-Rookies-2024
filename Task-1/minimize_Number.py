def maximum_(N,array):
    i = 0

    while all(num % 2 == 0 for num in array):
        array = [num // 2 for num in array]
        i += 1
    return i     
   
N = int(input())
array = list(map(int, input().split()))

maximum = maximum_(N,array)

print(maximum)   
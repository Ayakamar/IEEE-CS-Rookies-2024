def sum_of_array(array, N):
    if N == 1:
        return array[0]
    else:
        return array[N-1] + sum_of_array(array, N-1)

N = int(input())
array = list(map(int,input().split()))

array_sum = sum_of_array(array, N)
result = array_sum / N
print(result)


def smallest_pair_(N, arr):
    min_sum = float('inf') 

    for i in range(N):
        for j in range(i + 1, N):
            sum_i = arr[i] + arr[j] + j - i
            min_sum = min(min_sum,sum_i)

    return min_sum

T = int(input())

for _ in range(T):
    N = int(input())
  
    arr = list(map(int, input().split()))
    
    result = smallest_pair_(N, arr)
    print(result)

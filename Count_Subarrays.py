def decreasing_subarrays(arr):
    count = 0
    n = len(arr)

    for start in range(n):
        for end in range(start + 1, n + 1):
            subarray = arr[start:end]
            if all(subarray[i] <= subarray[i + 1] for i in range(len(subarray) - 1)):
                count += 1

    return count
def test_case():
    
    n = int(input())
   
    arr = list(map(int, input().split()))

    result = decreasing_subarrays(arr)

    print(result)

t = int(input())

for _ in range(t):
    test_case()

# Function to find the maximum number in each sub-array
def find_max_in_subarrays(arr):
    result = []
    n = len(arr)

    for i in range(n):
        max_num = float('-inf')
        for j in range(i, n):
            max_num = max(max_num, arr[j])
            result.append(max_num)

    return result

# Function to process each test case
def process_test_case():
    # Input the number of elements in the array
    n = int(input())
    
    # Input the array
    arr = list(map(int, input().split()))

    # Find the maximum number in each sub-array
    result = find_max_in_subarrays(arr)

    # Output the result
    print(*result)

# Input the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    process_test_case()

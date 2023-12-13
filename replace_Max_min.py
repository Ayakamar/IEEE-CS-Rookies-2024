N = int(input())
array = list(map(int, input().split()))

min_index = array.index(min(array))
max_index = array.index(max(array))

# Swap the minimum and maximum elements
array[min_index], array[max_index] = array[max_index], array[min_index]

# Print the updated array
print(*array)

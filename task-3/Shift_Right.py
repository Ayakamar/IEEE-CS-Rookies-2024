def shift_right_by_value(A, x, N):
    if N > 1:
        x %= N  # Ensure x is within the array size. If x is greater than or equal to the length of the array (n), the effective shift amount becomes x % n
        A = A[-x:] + A[:-x]
    return A

N, x = map(int, input().split())
A = list(map(int, input().split()))
New_array = shift_right_by_value(A, x, N)
print(*New_array)

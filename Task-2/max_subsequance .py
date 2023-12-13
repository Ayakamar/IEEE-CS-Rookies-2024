def max_subsequence_size(S,N)
    max_size = 1 
    for i in range(1, N):
        if S[i] != S[i-1]:  
            max_size += 1  
    return min(max_size, N)  

N = int(input())
S = input()

print(max_subsequence_size(S,N)))

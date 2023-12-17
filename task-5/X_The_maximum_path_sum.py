def max_path_sum(matrix, row, col, N, M):
    
    if row == N-1 and col == M-1:
        return matrix[row][col]
    if row == N-1:
        return matrix[row][col] + max_path_sum(matrix,row,col+1,N,M)
    elif col == M-1:
        return matrix[row,col] + max_path_sum(matrix,row + 1, col,N,M)
    else :
        return max(matrix[row][col] + max_path_sum(matrix,row,col+1,N,M),
                    matrix[row,col] + max_path_sum(matrix,row + 1, col,N,M))
                   

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = max_path_sum(matrix, 0, 0, N, M)
print(result)
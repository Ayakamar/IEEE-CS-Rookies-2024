def numbers_1_to_N(N):
    if N == 1:
        print("1")
    else :
        numbers_1_to_N(N-1)
        print(N) 

N = int(input())
numbers_1_to_N(N)


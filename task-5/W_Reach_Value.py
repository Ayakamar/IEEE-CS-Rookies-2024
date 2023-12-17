def Reach_Value(start, end):
    if start == end:
        return True
    elif start > end:
        return False
    
    return Reach_Value(start * 10, end) or Reach_Value(start * 20, end)

T = int(input())
for _ in range(T):
    N = int(input())
    result=Reach_Value(1, N)
    if result == True :
        print("YES")
    else :
        print("NO")    

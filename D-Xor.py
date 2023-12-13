def function(A,B,Q):
   
    if Q == 1:
        return A 
    elif Q ==2 :
        return B 
    elif Q >= 3:
        if Q %3 ==0:
            return A^B
         
        else:
            if (Q+1)%3 ==0:
                return B
            else :
                return A

A, B, Q = map(int, input().split())
result = function(A,B,Q)
print(result)    
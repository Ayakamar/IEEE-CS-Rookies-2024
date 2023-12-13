X1,Y1,X2,Y2=map(int,input().split())
X3,Y3,X4,Y4=map(int,input().split())
c_A_X=X1-X2
c_A_Y=Y1-Y2
c_B_X=X3-X4
c_B_Y=Y3-Y4

M=((c_A_X-c_B_X)**2-(c_A_Y-c_B_Y)**2)**.5  #The distance between the centers of the two circles
dimA=(((X1-X2)**2-(Y1-Y2)**2)**.5)/2 
dimB=(((X3-X4)**2-(Y3-Y4)**2)**.5)/2
if dimA + dimB < M :
    print("YES")
else :
    print("NO")    

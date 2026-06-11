n=10
for i in range(1,n):
    for j in range(1,n):
        if (i+j==n and i>=5) or (i==j and i>=5) or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(1,n):
    for j in range(1,n):
        if  j==1 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
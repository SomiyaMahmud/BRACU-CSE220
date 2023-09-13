def array_series(n):
    A=[0]*(n**2)
    i= 1
    while (i<=n):
        j= 1
        while (j<=i):
            A[(i*n)-j]= j
            j=j+1
        i=i+1
    return A
n = int(input())
print(array_series(n))
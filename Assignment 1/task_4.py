def rotateRight(source,k):
    j=0
    while j<k:
        i=len(source)-1
        x=source[i]
        while i>0:
            source[i]=source[i-1]
            i=i-1
        source[0]=x
        j=j+1
    return source
source=[10,20,30,40,50,60]
print(rotateRight(source,3))
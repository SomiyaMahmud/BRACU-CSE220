def ShiftRight(source,k):
    j=0
    while j<k:
        i=len(source)-1
        while (i>0):
          source[i]=source[i-1]
          i-=1
        source[0]=0
        j+=1
    return source
source = [10,20,30,40,50,60]
print(ShiftRight(source,3))
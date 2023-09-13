def ShiftLeft(source,k):
    j=0
    while j<k:
        i=0
        while (i<len(source)-1):
          source[i]=source[i+1]
          i+=1
        source[i]=0
        j+=1
    return source
source = [10,20,30,40,50,60]
print(ShiftLeft(source,3))
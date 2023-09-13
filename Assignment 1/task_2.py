def rotateLeft(source,k):
    j=0
    while j<k:
        i=0
        x=source[i]
        while (i<len(source)-1):
          source[i]=source[i+1]
          i+=1
        source[i]=x
        j+=1
    return source
source = [10,20,30,40,50,60]
print(rotateLeft(source,3))
def remove(source,size,idx):
    source[idx]=0
    i=idx+1
    while i<len(source):
        source[i-1]=source[i]
        i=i+1
    return source

def removeAll(source, size, element):
    i=0
    while i<size:
      if source[i]==element:
          remove(source,size,i)
          size-=1
      else:
          i+=1
    return source
source=[10,2,30,2,50,2,2,0,0]
print(removeAll(source,7,2))
def remove(source,size,idx):
    source[idx]=0
    i=idx+1
    while i<len(source):
        source[i-1]=source[i]
        i=i+1
    return source

source=[10,20,30,40,50,0,0]
print(remove(source,5,2))
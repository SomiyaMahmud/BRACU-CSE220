def repetition(A):
    temp=0
    for i in range(len(A)-1):
        if A[i]>A[i+1]:
            temp=A[i]
    arr=[0]*(temp+1)
    for j in range(len(A)):
         arr[A[j]]+=1

    arr2=[0]*len(arr)
    flag=False
    for k in range(len(arr)):
        if arr[k]>1:
          for l in range(k,len(arr2)):
               if arr[k] not in arr2:
                   arr2[l]=arr[k]
               else:
                   flag=True
                   break
               break
    return flag
A=[3,4,6,3,4,7,4,6,8,6,6]
print(repetition(A))
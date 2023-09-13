def max_bunch(A):
   temp=A[0]
   count=0
   max_count=0
   for i in range(len(A)):
       if A[i]==temp:
           count+=1
       else:
           count=1
           temp=A[i]
       if count>max_count:
            max_count=count
   return max_count
A= [1,1,2, 2, 1, 1,1,1]
print(max_bunch(A))
def splitting_array(A):
  left=0
  right=0
  flag=False
  for i in range(0,len(A)):
       left+=A[i]
  for j in range(0,len(A)):
       right+=A[j]
       left-=A[j]
       if left<right:
        break
       elif left==right:
        flag=True
  return flag
A= [10, 3, 1, 2, 10]
print(splitting_array(A))
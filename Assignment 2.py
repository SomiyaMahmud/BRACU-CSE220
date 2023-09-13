class CircularArray:
       def __init__(self, lin, st, sz):
            self.start = st
            self.size = sz
            self.lin=lin
            self.cir = [None]*len(self.lin)
            i=0
            j=self.start
            c=0
            while c<self.size:
                self.cir[j]=self.lin[i]
                i=i+1
                j=j+1
                if j>=len(self.cir):
                    j=0
                c=c+1
       def printFullLinear(self):
            for i in range(len(self.cir)):
                if i==len(self.cir)-1:
                    print(self.cir[i])
                else:
                    print(self.cir[i],end=',')

       def printForward(self):
            i=self.start
            c=0
            while c<self.size:
               print(self.cir[i],end=', ')
               i=i+1
               if i>=len(self.cir):
                   i=0
               c=c+1
            print(' ')

       def printBackward(self):
            last=((self.start+self.size)-1)%len(self.cir)
            c=0
            while c<self.size:
                print(self.cir[last],end=',')
                last=last-1
                if last<0:
                    last=len(self.cir)-1
                c=c+1
            print(' ')

       def linearize(self):
            self.new_lin=[None]*self.size
            i=self.start
            j=0
            c=0
            while c<self.size:
                self.new_lin[j]=self.cir[i]
                i=i+1
                j=j+1
                if i>=len(self.cir):
                    i=0
                c=c+1
            self.cir=self.new_lin


       def resizeStartUnchanged(self,n_size):
            self.n_size=n_size
            self.new_arr=[None]*self.n_size
            i=self.start
            j=self.start
            c=0
            while c<self.size:
                self.new_arr[i]=self.cir[j]
                i=i+1
                j=j+1
                if j>=len(self.cir):
                   j=0
                c=c+1
            self.cir=self.new_arr


       def palindromeCheck(self):
          middle=len(self.cir)//2
          last=((self.start+self.size)-1)%len(self.cir)
          for i in range(middle):
             if self.cir[self.start]==self.cir[last]:
               return 'This array is a palindrome'
             return 'This array is NOT a palindrome'

       def sort(self):
            for i in range(self.size-1):
                a= (i+self.start)%len(self.cir)
                for j in range(self.size-1-i):
                   b= (j+self.start)%len(self.cir)
                   c= (b+1)%len(self.cir)
                   if self.cir[b]>self.cir[c]:
                        x= self.cir[b]
                        self.cir[b]=self.cir[c]
                        self.cir[c]=x
       def equivalent(self, arr):
            flag=True
            for i in range(self.size):
                a=(i+self.start)%len(self.cir)
                b=(i+arr.start)%len(arr.cir)
                if self.cir[a] != arr.cir[b]:
                    flag=False
            return flag


       def intersection(self, c2):
           x=''
           for i in range(self.size):
                a=(i+self.start)%len(self.cir)
                for j in range(c2.size):
                    b=(j+c2.start)%len(c2.cir)
                    if self.cir[a] == c2.cir[b]:
                       x+=str(self.cir[a])+' '
           return x



lin_arr1 = [10, 20, 30, 40, None]
print("==========Test 1==========")
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.printForward() # This should print: 10, 20, 30, 40
c1.printBackward() # This should print: 40, 30, 20, 10
print("==========Test 2==========")
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40
print("==========Test 3==========")
lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None
print("==========Test 4==========")
lin_arr3 = [10, 20, 30, 20, 10, None, None]
c3 = CircularArray(lin_arr3, 3, 5)
c3.printForward() # This should print: 10, 20, 30, 20, 10
c3.palindromeCheck() # This should print: This array is a palindrome
print("==========Test 5==========")
lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome
print("==========Test 6==========")
lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
#c5.printFullLinear()
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50
print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30, None]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True
print("==========Test 8==========")
lin_arr7 = [10, 20, -30, 20, 50, 30, None, None, None]
c8 = CircularArray(lin_arr7, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c8.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c8)) # This should print: True
print("==========Test 9==========")
lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False
print("==========Test 10==========")
lin_arr9 = [10, 20, 30, 40, 50, None, None, None]
c10 = CircularArray(lin_arr9, 5, 5)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 7)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]
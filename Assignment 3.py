class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n

class LinkedList:

  def __init__(self, a):
    if type(a)==list:
      self.head=None
      n=Node(a[0],None)
      self.head=n
      for i in range(1,len(a)):
          x=Node(a[i],None)
          p=x
          n.next=p
          n=x
    else:
        self.head=a

  def countNode(self):
        count=0
        p=self.head
        while p!=None:
            count+=1
            p=p.next
        return count

  def printList(self):
      h=self.head
      while h!=None:
          print(h.element,end=',')
          h=h.next
      print(' ')

  def nodeAt(self, idx):
      count=0
      h=self.head
      if idx<0:
          return None
      while h!=None:
          if count==idx:
              return h
          count+=1
          h=h.next


  def get(self, idx):
      count=0
      h=self.head
      if idx<0:
          return None
      while h!=None:
          if count==idx:
              return h.element
          count+=1
          h=h.next

  def set(self, idx, elem):
      count=0
      h=self.head
      if idx<0:
          return None
      while h!=None:
          if count==idx:
              s=h.element
              h.element=elem
              return s
          count+=1
          h=h.next
  def indexOf(self, elem):
      i=0
      h=self.head
      while h!=None:
           if h.element==elem:
               return i
           i=i+1
           h=h.next
      return -1

  def contains(self, elem):
      a=self.head
      while a!=None:
            if a.element==elem:
                return True
            else:
                a=a.next
      return False


  def copyList(self):
      h=self.head
      n=Node(h.element,None)
      cont=n
      h=h.next
      while h!=None:
          x=Node(h.element,None)
          n.next=x
          n=x
          h=h.next
      return cont


  def reverseList(self):
      prev=None
      cur=self.head
      while cur!=None:
          next=cur.next
          cur.next=prev
          prev=cur
          cur=next
      return prev

  def insert(self, elem, idx):
        n=Node(elem,None)
        if idx==0:
            n.next=self.head
            self.head=n
        elif idx==self.countNode():
            h=self.head
            while h.next!=None:
                h=h.next
            h.next=n
        else:
            h=self.head
            i=0
            while i<idx-1:
                h=h.next
                i=i+1
            x=h.next
            n.next=x
            h.next=n


  def remove(self, idx):
        if idx==0:
            l=self.head.next
            x=self.head
            self.head=None
            self.head=l
            return x.element
        elif idx==(self.countNode()-1):
            l=self.head
            while l.next.next!=None:
                l=l.next
            k=l.next.element
            l.next=None
            return k
        else:
            i=0
            l=self.head
            while i<idx-1:
                l=l.next
                i=i+1
            d=l.next
            x=d.next
            l.next=x
            k=d.element
            d=None
            return k

  def rotateLeft(self):
                n=self.head
                self.head=self.head.next
                n.next=None
                h=self.head
                while h.next!=None:
                    h=h.next
                h.next=n


  def rotateRight(self):
      n=None
      h=self.head
      while h.next.next!=None:
            h=h.next
      n=h.next
      h.next=None
      n.next=self.head
      self.head=n

print("////// Test 01 //////")
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1)
h1.printList() # This should print: 10,20,30,40
print(h1.countNode()) # This should print: 4


print("////// Test 02 //////")
myNode = h1.nodeAt(1)
print(myNode.element)


print("////// Test 03 //////")
val = h1.get(2)
print(val) # This should print: 30. In case of invalid index This will print None.


print("////// Test 04 //////")
print(h1.set(1,85)) # This should print: 20
h1.printList() # This should print: 10,85,30,40.
print(h1.set(15,85)) # This should print: None
h1.printList() # This should print: 10,85,30,40.


print("////// Test 05 //////")
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that doesn't exists in the list this will print -1.


print("////// Test 06 //////")
ask = h1.contains(40)
print(ask) # This should print: True.


print("////// Test 07 //////")
a2 = [10,20,30,40,50,60,70]
h2 = LinkedList(a2) # uses theconstructor where a is an built in list
h2.printList() # This should print: 10,20,30,40,50,60,70.
# Makes a duplicate copy of the given List. Returns the head reference of the duplicate list.
copyH=h2.copyList() # Head node reference of the duplicate list
h3 = LinkedList(copyH) # uses the constructor where a is head of a linkedlist
h3.printList() # This should print: 10,20,30,40,50,60,70.



print("////// Test 08 //////")
a4 = [10,20,30,40,50]
h4 = LinkedList(a4) # uses theconstructor where a is an built in list
h4.printList() # This should print: 10,20,30,40,50.
# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
revH=h4.reverseList() # Head node reference of the reversed list
h5 = LinkedList(revH) # uses the constructor where a is head of a linkedlist
h5.printList() # This should print: 50,40,30,20,10.


print("////// Test 09 //////")
a6 = [10,20,30,40]
h6 = LinkedList(a6) # uses theconstructor where a is an built in list
h6.printList() # This should print: 10,20,30,40.
h6.insert(85,0)
h6.printList() # This should print: 85,10,20,30,40.
h6.insert(95,3)
h6.printList() # This should print: 85,10,20,95,30,40.
h6.insert(75,6)
h6.printList() # This should print: 85,10,20,95,30,40,75.

print("////// Test 10 //////")
a7 = [10,20,30,40,50,60,70]
h7 = LinkedList(a7) # uses theconstructor where a is an built in list
h7.printList() # This should print: 10,20,30,40,50,60,70.
print("Removed element:",h7.remove(0)) # This should print: Removed element: 10
h7.printList() # This should print: 20,30,40,50,60,70.
print("Removed element: ",h7.remove(3)) # This should print: Removed element: 50
h7.printList() # This should print: 20,30,40,60,70.
print("Removed element: ",h7.remove(4)) # This should print: Removed element: 70
h7.printList() # This should print: 20,30,40,60.

print("////// Test 11 //////")
a8 = [10,20,30,40]
h8 = LinkedList(a8) # uses theconstructor where a is an built in list
h8.printList() # This should print: 10,20,30,40.
h8.rotateLeft()
h8.printList() # This should print: 20,30,40,10.

print("////// Test 12 //////")
a9 = [10,20,30,40]
h9 = LinkedList(a9) # uses theconstructor where a is an built in list
h9.printList() # This should print: 10,20,30,40.
h9.rotateRight()
h9.printList() # This should print: 40,10,20,30.
class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p

class DoublyList:
  def __init__(self, a):
      n=Node(None,None,None)
      self.head=n
      for i in range(len(a)):
          x=Node(a[i],None,None)
          n.next=x
          x.prev=n
          n=x
      n.next=self.head
      self.head.prev=n
  def countNode(self):
        count=0
        start_node=self.head.next
        while start_node!=self.head:
            count+=1
            start_node=start_node.next
        return count

  def forwardprint(self):
      start_node=self.head.next
      while start_node!=self.head:
          print(start_node.element,end=',')
          start_node=start_node.next
      print(' ')


  def backwardprint(self):
      start_node=self.head.prev
      while start_node!=self.head:
        print(start_node.element,end=',')
        start_node=start_node.prev
      print(' ')


  def nodeAt(self, idx):
      count=0
      start_node=self.head.next
      if idx<0:
          return None
      while start_node!=self.head:
          if count==idx:
              return start_node
          count+=1
          start_node=start_node.next

  def indexOf(self, elem):
      i=0
      start_node=self.head.next
      while start_node!=self.head:
           if start_node.element==elem:
               return i
           i=i+1
           start_node=start_node.next
      return -1


  def insert(self, element, idx):
      new_node=Node(element,None,None)
      i=0
      start_node=self.head.next
      while(i<idx):
          start_node=start_node.next
          i=i+1
      prev_node=start_node.prev
      new_node.next = start_node
      start_node.prev =new_node
      prev_node.next =new_node
      new_node.prev=prev_node
      return new_node
  def remove(self, idx):
      i=0
      start_node=self.head.next
      while(i<idx):
          start_node=start_node.next
          i=i+1
      prev_node=start_node.prev
      removed_node=prev_node.next
      next_node=start_node.next
      next_node.prev=prev_node
      prev_node.next=next_node
      return str(removed_node.element)

print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array
h1.forwardprint() # This should print: 10,20,30,40.
h1.backwardprint() # This should print: 40,30,20,10.
print(h1.countNode()) # This should print: 4
print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"
print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that
#doesn't exists in the list this will print -1.
print("///  Test 04  ///")
a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.
# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40.
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.
h2.backwardprint() # This should print: 40,30,95,20,10,80.

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75.
h2.backwardprint() # This should print: 75,40,30,95,20,10,85.
print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.
h3.backwardprint() # This should print: 70,60,50,40,30,20.
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.
h3.backwardprint() # This should print: 70,60,40,30,20.
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60.
h3.backwardprint() # This should print: 60,40,30,20.
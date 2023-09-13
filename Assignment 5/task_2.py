class Node:
    def __init__(self,e,n):
        self.elem=e
        self.next=n

class LStack:
    def __init__(self):
        self.head=Node(None,None)

    def push(self,e):
        n=Node(e,None)
        n.next=self.head.next
        self.head.next=n
    def pop(self):
        if self.head.next==None:
            raise Exception("Can't pop because the stack is empty")
        else:
           temp=self.head.next
           self.head.next=None
           self.head.next=temp.next

    def peek(self):
        return self.head.next.elem


    def paranthesis_check(self,op,cl):
        if op=="(" and cl==")":
            return True
        elif op=="{" and cl=="}":
           return True
        elif op=="[" and cl=="]":
          return True
        else:
          return False
    def paranthesis_balancing(self,exp):
        flag=True
        L_open= ['(','{','[']
        L_close= [')','}',']']
        for i in range(len(exp)):
            if exp[i] in L_open or exp[i] in L_close:
                if exp[i] in L_open:
                  self.push(exp[i])
                else:
                  if self.head.next==None:
                    flag=False
                    break
                  else:
                    flag= self.paranthesis_check(self.peek(),exp[i])
                    if flag==True:
                        self.pop()
                    else:
                        break
        if flag==True:
            print('This expression is correct.')
        else:
            if self.head.next==None :
              print('This expression is NOT correct.')
              print(f"Error at character # {i+1}. '{exp[i]}' - not opened.")
            elif flag==False:
                print('This expression is NOT correct.')
                for j in range(len(exp)):
                        if exp[j]==self.peek():
                           print(f"Error at character # {j+1}. '{exp[j]}' - not closed.")

exp=input()
s1=LStack()
s1.paranthesis_balancing(exp)
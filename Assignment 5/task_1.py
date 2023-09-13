class Stack:
    def __init__(self):
        self.arr=[0]*10
        self.top=-1
    def push(self,x):
        if self.top==(len(self.arr)-1):
            raise Exception('Can"t push because the stack is full')
        else:
            self.top=self.top+1
            self.arr[self.top]=x

    def pop(self):
        if self.top==-1:
            print('error')
        else:
            re=self.arr[self.top]
            self.arr[self.top]=0
            self.top-=1

    def peek(self):
        return self.arr[self.top]

    def paranthesis_check(self,op,cl):
        if op=='('and cl==')':
            return True
        elif op== '{' and cl=='}':
           return True
        elif op=='[' and cl==']':
          return True
        else:
          return False

    def paranthesis_balancing(self,exp):
        flag=True
        L_open= ['(','{','[']
        L_close= [')','}',']']
        for i in range(0,len(exp)):
            if exp[i] in L_open or exp[i] in L_close:
              if exp[i] in L_open:
                self.push(exp[i])

              else:
                if self.top==-1:
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
            if self.top!=-1:
              print('This expression is NOT correct.')
              for j in range(len(exp)):
                        if exp[j]==self.peek():
                           print(f"Error at character #{j+1}. '{exp[j]}' - not closed.")


            elif flag==False:
                print('This expression is NOT correct.')
                print(f"Error at character #{i+1}. '{exp[i]}' - not opened.")




exp=input()
s1=Stack()
s1.paranthesis_balancing(exp)
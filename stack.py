def push_e():
    if len(s)==n:
        print("Stack is full!")
    else:
        e=input("Enter the element to insert")
        s.append(e)
        print(s)

def pop_e():
    if(s==0):
        print("Stack is empty..Add data items")
    else:        
        e=s.pop()
        print(e,"removed")
s=[]
n=int(input("Enter the size of the stack:"))
while True:
    print("Enter the operation\n1.push\n2.pop\n3.Quit")
    c=int(input())
    if c==1:
        push_e()
    elif c==2:
        pop_e()
    elif c==3:
        break
    else:
        print("Enter the correct operation:")


    

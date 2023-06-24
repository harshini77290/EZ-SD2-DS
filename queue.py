def enq():
    if len(q)==n:
        print("Queue is full!")
    else:
        e=input("Enter the element to insert")
        q.append(e)
        print(q)

def deq():
    if(q==0):
        print("Queue is empty..Add data items")
    else:        
        e=q.pop(0)
        print(e,"removed")
q=[]
n=int(input("Enter the size of the Queue:"))
while True:
    print("Enter the operation\n1.Enqueue\n2.Dequeue\n3.Quit")
    c=int(input())
    if c==1:
        enq()
    elif c==2:
        deq()
    elif c==3:
        break
    else:
        print("Enter the correct operation:")


    

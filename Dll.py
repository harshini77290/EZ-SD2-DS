class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        
class Dll:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end="")
                temp=temp.next

    def insert_begin(self,data):
        new_node=Node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    def insert_pos(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node

    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
        temp.next=None  

    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None

    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.prev=None
#print(dl.head)
       
node_1=Node("Harshini")
dl=Dll()
dl.head=node_1
node_2=Node("Abhi")
node_3=Node("Siri")
node_4=Node("Varsha")
node_5=Node("Shyni")

node_1.next=node_2
node_2.prev=node_1
node_2.next=node_3
node_3.prev=node_2
node_3.next=node_4
node_4.prev=node_3
node_4.next=node_5
node_5.prev=node_4

'''
print(node_2.prev.data,end="->")
print(node_3.prev.data,end="->")
print(node_4.prev.data,end="->")
print(node_5.prev.data,end="->")
print(node_4.next.data)
'''

dl.display()
print("\n\nAfter inserting at the beginning")
dl.insert_begin("Abhi")
dl.display()

print("\n\nAfter inserting at the end")
dl.insert_end("Aashish")
dl.display()

print("\n\nAfter inserting at pos 3")
dl.insert_pos(3,"pavan")
dl.display()

print("\n\nAfter deleting at the beginning")
dl.delete_beg()
dl.display()

print("\n\nAfter deleting at the end")
dl.delete_end()
dl.display()

print("\n\nAfter deleting at pos 2")
dl.delete_pos(2)
dl.display()


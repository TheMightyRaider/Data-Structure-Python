class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class Linkedlist:
    def __init__(self):
        self.head=None 
    
    def push(self,number):
        new_node=Node(number)
        temp=self.head
        new_node.next=self.head

        if(self.head is not None):
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
        else:
            new_node.next=new_node
        self.head=new_node

    def insertinbetween(self,previousnode,data):
        new_node=Node(data)
        current=self.head
        if(current is not None):
            while(current):
                if(current.data==previousnode):
                    new_node.next=current.next
                    current.next=new_node
                    break
                current=current.next
        else:
            print('List is Empty')

    def append(self,data):
        new_node=Node(data)
        last=self.head
        while(last.next!=self.head):
            last=last.next
        new_node.next=last.next
        last.next=new_node

    def deletebyvalue(self,value):
        current=self.head
        while(current):
            if(current.data==value):
                break
            prev=current
            current=current.next
        prev.next=current.next

    def deletebyposition(self,position):
        current=self.head
        if(position==1):
            self.head=current.next
            current=None 
            return
        
        for i in range(position-2):
            current=current.next
        current.next=current.next.next

    def print(self):
        current=self.head
        while(current is not None):
            print(current.data)
            current=current.next
            if(current==self.head):
                break

# TESTING

circularlinkedlist=Linkedlist()
circularlinkedlist.push(1)
circularlinkedlist.push(2)
circularlinkedlist.push(3)
circularlinkedlist.insertinbetween(2,5)
circularlinkedlist.append(7)
circularlinkedlist.deletebyvalue(1)
circularlinkedlist.deletebyposition(4)
circularlinkedlist.print()
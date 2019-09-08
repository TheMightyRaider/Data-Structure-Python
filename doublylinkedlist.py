class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
        self.prev=None 

class DoublyLinkedList:
    def __init__(self):
        self.head=None 

    def insert(self,newnode):
        new_node=Node(data=newnode)
        new_node.next=self.head
        new_node.prev=None
        if self.head is not None:
            self.head.prev=new_node 
        self.head=new_node
        
    def insertinbetween(self,previousnode,newnode):
            new_node=Node(data=newnode)
            first=self.head
            while(first is not None):
                 if(first.data==previousnode):
                     break
                 first=first.next
            new_node.next=first.next
            first.next=new_node
            new_node.prev=first

    def deletebyvalue(self,value):
        current=self.head
        if(current.data==value):
            self.head=current.next
            return

        while(current):
            if(current.data==value):
                break
            current=current.next
        current.prev.next=current.next


    def deletebyposition(self,position):
        current=self.head
        if(position==1):
            current.next=self.head

        for i in range(1,position-1):
            current=current.next
        current.next=current.next.next
    
    def print(self):
        current=self.head
        while(current):
            print(current.data)
            current=current.next

linkedlist=DoublyLinkedList()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(7)
linkedlist.insertinbetween(1,3)
linkedlist.deletebyvalue(3)
linkedlist.deletebyposition(2)
linkedlist.print()

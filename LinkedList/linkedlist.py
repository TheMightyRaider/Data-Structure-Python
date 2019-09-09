class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,newnode):
        new_node=Node(newnode)
        new_node.next=self.head
        self.head=new_node

    def append(self,newnode):
        new_node=Node(newnode)
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
            
    def deletebyValue(self,newnode):
        first=self.head

        if(first.data==newnode):
            self.head=first.next
            first.next=None
            return

        while(first is not None):
            if(first.data==newnode):
                break
            prev=first
            first=first.next
        prev.next=first.next
    
    def deletebyPostition(self,position):
        first=self.head
        if position==0:
            self.head=first.next
            first=None
            return
        # Previous Node
        for i in range(position-1):
            first=first.next
        nextelement=first.next.next
        first.next=nextelement


    def printlist(self):
        temp=self.head
        while(temp):
            nodedata=temp.data
            print(nodedata)
            temp=temp.next
    
    def insertinbetween(self,previous_node,newnode):
        new_node=Node(newnode)
        new_node.next=previous_node.next
        previous_node.next=new_node
        
linkedlist=LinkedList()
linkedlist.push(0)
secondlist=Node(2)
thirdlist=Node(3)

linkedlist.head.next=secondlist
secondlist.next=thirdlist

linkedlist.push(1)
linkedlist.push(2)

linkedlist.insertinbetween(linkedlist.head,4)
linkedlist.insertinbetween(secondlist,3)

linkedlist.append(5)

linkedlist.deletebyValue(2)
linkedlist.deletebyPostition(1)

linkedlist.printlist()

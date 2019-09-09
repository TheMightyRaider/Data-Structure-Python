class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
        self.prev=None

class QueueUsingLinkedList:
    def __init__(self):
        self.head=None 

    def enqueue(self,data):
        new_node=Node(data)
        new_node.next=self.head
        new_node.prev=None
        if(self.head is not None):
            self.head.prev=new_node
        self.head=new_node
        
    def dequeue(self):
        current=self.head
        if(current is not None):
            while(current.next!=None):
                current=current.next
            current.prev.next=current.next
        else:
            print('UnderFlow')
           
    def print(self):
        current=self.head
        if (current is not None):
            while(current):
                print(current.data)
                current=current.next
        else:
            print('Queue is Empty')
        
        
queue=QueueUsingLinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()

queue.print()
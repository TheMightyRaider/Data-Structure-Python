class Node:
    def __init__(self,data,priority):
        self.data=data
        self.next=None
        self.priority=priority
    
class PriorityQueueLinkedlist:
    def __init__(self):
        self.head=None

    def enqueue(self,data,priority):
        new_node=Node(data,priority)
        temp=self.head
        if(temp is not None):
            if(temp.priority<new_node.priority):
                new_node.next=self.head.next
                self.head.next=new_node
                self.head=temp
            else:
                new_node.next=self.head
                self.head=new_node
        else:
              new_node.next=self.head
              self.head=new_node
            
    def dequeue(self):
        current=self.head
        if(current is not None):
            while(current.next!=None):
                prev=current
                current=current.next
            prev.next=current.next
        
        else:
            print("UnderFlow")

    def print(self):
        current=self.head
        while(current):
            print(current.data)
            current=current.next

priorityQueue=PriorityQueueLinkedlist()
priorityQueue.enqueue(1,3)
priorityQueue.enqueue(2,1)
priorityQueue.enqueue(3,2)
priorityQueue.dequeue()
priorityQueue.print()


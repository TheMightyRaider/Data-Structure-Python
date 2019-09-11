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
        current=self.head
        if(current==None):
            new_node.next=current
            self.head=new_node
            return

        elif(current.next==None):
            if(current.priority<new_node.priority):
                new_node.next=current.next
                current.next=new_node
                self.head=current
                return
            else:
                new_node.next=current
                self.head=new_node 
                return
        else:
            if(current.priority<new_node.priority):
                while(current and current.priority<new_node.priority):
                    previous=current
                    current=current.next
                previous.next=new_node
                new_node.next=current
            else:
                new_node.next=current
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
priorityQueue.enqueue('Vishnu',5)
priorityQueue.enqueue('Sriram',10)
priorityQueue.enqueue('Rihan',3)
priorityQueue.enqueue('Rihanxx',4)
priorityQueue.dequeue()
priorityQueue.print()


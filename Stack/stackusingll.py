class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class StackUsingLinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        current=self.head
        if(current is not None):
            self.head=current.next
            current=None
        else:
            print('UnderFlow')

    def print(self):
        current=self.head
        if(current is not None):
             while(current):
                print(current.data)
                current=current.next
        else:
            print('Stack is Empty')

stack=StackUsingLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.print()
class Queue():
    def __init__(self):
        self.data=[]
        
    def enqueue(self,number):
        self.data.append(number)

    def dequeue(self):
        self.data.pop(0)
        
    def display(self):
        print(self.data)
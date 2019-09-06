# -------- USING CLASS --------

class Stack:
    def __init__(self):
        self.data=[]

    def isEmpty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def push(self, item):
        self.data.append(item)

    def pop(self):
        self.data.pop()
    
    def display():
        print(self.data)
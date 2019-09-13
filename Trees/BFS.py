class Node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 

class Tree:
    def __init__(self):
        self.root=None 

    def insert(self,value):
        root=self.root
        if root is None:
            new_node=Node(value)
            self.root=new_node
        else:
            new_node=Node(value)
            q=[]
            q.append(root)
            while(len(q)):
                temp=q.pop(0)
                if(not temp.left):
                    temp.left=new_node
                    break
                else:
                    q.append(temp.left)
                if(not temp.right):
                    temp.right=new_node
                    break
                else:
                    q.append(temp.right)
            
    def BFSprint(self):
        root=self.root
        q=[]
        q.append(root)
        if(root is None):
            return
        while(len(q)):
            temp=q.pop(0)
            print(temp.data)
            if(temp is None):
                continue
            if(temp.left):
                q.append(temp.left)
            if(temp.right):
                q.append(temp.right)
        
binarytree=Tree()
binarytree.insert(1)
binarytree.insert(2)
binarytree.insert(3)
binarytree.insert(4)
binarytree.insert(5)                
binarytree.BFSprint()

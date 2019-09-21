class Node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 
        self.height=0

class AVL:
    def __init__(self,root):
        self.root=None 

    def insert(self,key):
        root=self.root
        current=root
        if current is None:
            return Node(key)
        elif key<root.data:
            current=self.root.left
            root.left=self.insert(key)
        else:
            current=self.root.right
            root.right=self.insert(key)

        root.height=1+max(self.findheight(root.left),self.findheight(root.right))
        balance=self.findbf(root)
        if balance > 1 and key < root.left.data:
            return self.rightrotate(root)
        if balance < -1 and key > root.right.data:
            return self.leftrotate(root)
        if balance > 1 and key > root.left.data:
            root.left=self.leftrotate(root.left)
            return self.rightrotate(root)
        if balance < 1 and key < root.right.data:
            root.right=self.rightrotate(root.right)
            return self.leftrotate(root)

        return root
        
        
    def rightrotate(self,x):
        temp=x.left
        right=temp.right

        temp.right=x
        x.left=right

        x.height=1+max(self.findheight(x.left),self.findheight(x.right))
        temp.height=1+max(self.findheight(temp.left),self.findheight(temp.right))

        return temp

    def leftrotate(self,x):
        temp=x.right
        left=temp.left

        temp.left=x
        x.right=left

        x.height=1+max(self.findheight(x.left),self.findheight(x.right))
        temp.height=1+max(self.findheight(temp.left),self.findheight(temp.right))
        return temp

    def findbf(self,root):
        if not root:
            return 0
        return self.findheight(root.left)-self.findheight(root.right)

    def findheight(self,root):
        if not root:
            return 0

        return root.height

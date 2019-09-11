class Node():
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 

class Tree():
    def __init__(self):
        self.root=None 

    def insert(self,value):
        if (self.root is None):
            new_node=Node(value)
            self.root=new_node
            return self.root
        else:
            new_node=Node(value)
            q=[]
            q.append(self.root)
        
            while(len(q)):
                temp=q[0]
                q.pop()
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

    def inorder(self,root):
        if(not root):
            return
        self.inorder(root.left)
        print(root.data,end=' ')
        self.inorder(root.right)

binarytree=Tree()
root=binarytree.insert(10)
binarytree.insert(11)
binarytree.insert(7)
binarytree.inorder(root)  
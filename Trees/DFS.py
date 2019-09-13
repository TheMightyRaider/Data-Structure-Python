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
            return self.root
        else:
            new_node=Node(value)
            q=[]
            q.append(root)
            while(len(q)):
                temp=q.pop(0)
                if(temp.left is None):
                    temp.left=new_node
                    break
                else:
                    q.append(temp.left)

                if(temp.right is None):
                    temp.right=new_node
                    break
                else:
                    q.append(temp.right)
        
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)

    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=' ')

dfstree=Tree()
root=dfstree.insert(1)
dfstree.insert(2)
dfstree.insert(3)
dfstree.insert(4)
dfstree.insert(5)
dfstree.inorder(root)
print('***')
dfstree.preorder(root)
print('***')
dfstree.postorder(root)


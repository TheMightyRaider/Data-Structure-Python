class Node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 

class BinaryTree:
    def __init__(self):
        self.root=None 

    def insert(self,data):
        current=self.root
        if(current is None):
            new_node=Node(data)
            self.root=new_node
            return self.root
        else:
            new_node=Node(data)
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
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=' ')
        self.inorder(root.right)

    def deletedeepestnode(self,value):
        root=self.root
        q=[]
        q.append(root)
        while(len(q)):
            temp=q.pop(0)
            if(temp is value):
                temp=None 
                return
            if(temp.right):
                if(temp.right is value):
                    temp.right=None 
                    return
                else:
                    q.append(temp.right)
            if(temp.left):
                if(temp.left is value):
                    temp.left=None 
                    return 
                else:
                    q.append(temp.left)

    def delete(self,value):
        root=self.root
        if root==None:
            return None
        if root.left==None and root.right==None:
            if(root.data==value):
                return None
            else:
                return None
        Node_key=None 
        q=[]
        q.append(root)
        while(len(q)):
            temp=q.pop(0)
            if(temp.data==value):
                Node_key=temp
            if(temp.left):
                q.append(temp.left)
            if(temp.right):
                q.append(temp.right)
        if(Node_key):
            deepestnode=temp.data
            self.deletedeepestnode(temp)
            Node_key.data=deepestnode

        else:
            print('Data not Found')

    
                
            

            
binarytree=BinaryTree()
root=binarytree.insert(10)
binarytree.insert(11)
binarytree.insert(7)
# binarytree.inorder(root)
binarytree.delete(11)
binarytree.inorder(root) 
            




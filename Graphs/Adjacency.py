class Graph:
    def __init__(self,size):
        self.adjMatrix=[]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size=size
    
    def insertedge(self,vertex1,vertex2):
        if(vertex1==vertex2):
            return
        else:
            self.adjMatrix[vertex1][vertex2]=1
            self.adjMatrix[vertex2][vertex1]=1

    def deleteedge(self,vertex1,vertex2):
        if(vertex1==vertex2):
            return
        else:
            self.adjMatrix[vertex1][vertex2]=0
            self.adjMatrix[vertex2][vertex1]=0

    def CheckEdge(self,vertex1,vertex2):
        return True if self.adjMatrix[vertex1][vertex2]>0 else print('Edge doesnt exist')

    def printgraph(self):
        for i in range(len(self.adjMatrix)):
            print(self.adjMatrix[i])       

g = Graph(5)
g.insertedge(0, 1)
g.insertedge(0, 2)
g.insertedge(1, 2)
g.insertedge(2, 0)
g.insertedge(2, 3)
g.insertedge(0,0)
g.deleteedge(0,1)
g.printgraph()
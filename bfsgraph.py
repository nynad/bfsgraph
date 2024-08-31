# graphs are a data structure in which data can be sorted in any order as long as they are all connected. 
# it's like a shape (that can be any form) with vertices 
# 
# BFS: 

class Graph():
    def __init__(self,max):
        self.max=max 
        self.adjacent=[[]*max for i in range(max)] # create a list of 4 empty sublists. each sublist holds a node value and it's neighbours.
    
    def createedge(self,x,y): # shows who is who's neightbour with x and y, it works both ways 
        self.adjacent[x-1].append(y-1)
        self.adjacent[y-1].append(x-1)

    def bfs(self,source):
        visited=[False]*self.max
        queue=[]
        temp=[]

        queue.append(source)
        while len(queue) > 0: 
            cn=queue.pop(0)
            temp.append(cn)
            for i in self.adjacent[cn]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        
        return temp 
    


graph=Graph(4)

graph.createedge(2,3)
graph.createedge(1,4)
graph.createedge(1,2)
graph.createedge(4,3)

print(graph.bfs(2))









    
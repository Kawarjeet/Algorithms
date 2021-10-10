# Bellman Ford Algorithm

# Notes:
# Bellman Ford Algorithm uses the Dynamic Programming approach in which all possible solutions are tried and the best one is picked up.

# Python Code:

class Graph:
  
    def __init__(self, vertices):
      self.V = vertices
      self.graph = []
      
    def addEdge(self, u, v, w):
      self.graph.append([u,v,w])
      
    def printArr(self, dist):
      for i in range(self.V)
        print("{0}\t\t{1}".format(i, dist[i]))
      
    def bellmand_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src]= 0
        
        for _ in range(self.V - 1):
          
          for u,v,w in self.graph:
            if dist[u]!=float("Inf") and dist[v]>dist[u]+w:
              dist[v] = dist[u] + w
        
        for u,v,w in self.graph:
          if dist[u]!= float("Inf") and dist[v] > dist[u] + w:
            print("negative weight cycle exitst")
            return
            
        
g = Graph(5)
g.addEdge(0,1,-1)
g.addEdge(0,2,4)
g.addEdge(2,2,3)
g.addEdge(1,3,2)
g.addEdge(1,4,2)
g.addEdge(3,2,1)
g.addEdge(4,3,-3)
g.bellman_ford(0)

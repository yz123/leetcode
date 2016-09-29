"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        #dfs
        #isIn = {}
        #return self.dfs(node, isIn)
        return self.bfs(node)
    
    #dfs
    def dfs(self, node, isIn):
        if node !=None:
            if id(node) not in isIn:
                newNode = UndirectedGraphNode(node.label)
                isIn[id(node)] = newNode
                for nei in node.neighbors:
                    newNode.neighbors.append(self.dfs(nei, isIn))
            else:
                newNode = isIn[id(node)]
            return newNode
        return None
        
    #bfs
    def bfs(self, node):
        if node == None:
            return None
        start = node
        isIn = {}
        q = []
        q.append(node)
        #create all nodes
        while len(q)!=0:
            node = q.pop(0)
            #print node.label
            if (node) not in isIn:
                newnode = UndirectedGraphNode(node.label)
                isIn[(node)] = newnode
                for nei in node.neighbors:
                    q.append(nei)
        #copy neighbors
        for node in isIn:
            isIn[(node)].neighbors = [ isIn[(nei)]  for nei in node.neighbors]
                
        return isIn[(start)]

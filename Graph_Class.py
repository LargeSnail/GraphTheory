import matplotlib.pyplot as plt
class Graph:
    def __init__(self, nodes, adjacency):
        self.nodes = nodes
        self.adjacency = adjacency
    
    def __add__(self,another_graph):
        out = Graph(list(),list())
        for x in self.nodes:
            out.add_node(x)
            for y in another_graph.nodes:
                out.add_node(y)
                out.join_nodes(x,y)
        return out
    def join_nodes(self,node1,node2):
        if not node1 in self.adjacency.keys():
            self.adjacency[node1.getLabel()] = [node2]
            self.adjacency[node2.getLabel()] = [node1]
        else:
            (self.adjacency[node1.getLabel()]).append(node2)
            (self.adjacency[node2.getLabel()]).append(node1)

       
    def add_node(self,node):
        self.nodes.append(node)
    def toString(self):
        out = 'Nodes: '
        for x in self.nodes:
            out = out + '('+x.toString()
            out = out + ', '
            out = out + 'Connections: '
            out = out + str(self.adjacency[x])+')'
        out = out +')'
       

        return  out
class Node:
    def __init__(self,value,label):
        self.value = value
        self.label = label

    def getValue(self):
        return self.value()
    
    def setValue(self,value):
        self.value = value
    def setLabel(self,label):
        self.label = label
    def getLabel(self):
        return self.label
    #######################################################################
    #Deprecated Code
    #Functionality is in the Graph class
    #######################################################################
   # def addConnection(self,connection):
      #  self.connections.append(connection);
   # def removeConnection(self,connection):
      #  self.connections.remove(connection)
   # def getConnections(self):
      #  return self.connections();
    #######################################################################
    #End DeprecatedCode
    #######################################################################
    def toString(self):
        out = self.label +': '+str(self.value)+'\n'
        return out
#class Weighted_Node(Node):
    #def __init__(self,value,connections,weights):
node1 = Node(5,'1')
node2 = Node(6,'2')
graph1 = Graph([node1,node2],dict())
print(node1)
print(node2)
graph1.join_nodes( node1,node2)
node3 = Node(7,'3')
node4 = Node(8,'4')
graph2 = Graph([node3,node4],dict())
graph2.join_nodes(node3,node4)
graph3 = graph1+graph2
print(graph3.toString())

    
######################################################

import networkx as nx
import matplotlib.pyplot as plt
#This will create Kn, where you pass in the n and graph it.
def create_Kn(n):
    G = nx.Graph()
    for i in range(0,n ):
        G.add_node(i+1);
    for i in range(0,n):
        a = list(range(0,n));
        for j in range(0,n):
           if not j == i:
              G.add_edge(i+1,j+1)
    
   
    nx.draw(G)
    plt.show()


#create_Kn(1000)
create_Kn(6)

        

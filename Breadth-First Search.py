import matplotlib.pyplot as plt
import networkx as nx

def insert (node, node2, graph):
    if (node in graph):
        tempNode = graph[node]
        if (node2 not in tempNode):
            tempNode.append(node2)
        graph[node] = tempNode
    else:
        graph[node] = [node2]
    return graph

def BFS(Q,A,graph):
    print(Q)
    iterator = Q.pop()
    A.append(iterator)
    print(A)
    print(Q)
    print(graph)


def startUp(vectores):
    graph = {}

    # hacer los renglones arrays de int
    for node in vectores:
        # checar que no este vacio
        if (node == ""):
            vectores.remove(node)
        else:
            # separar valores y node
            nodeVal = int(node[1])
            nodePoint = int(node[3])

            G.add_edge(nodeVal, nodePoint)
            graph = insert(nodeVal, nodePoint, graph)
            graph = insert(nodePoint, nodeVal, graph)
    return graph


input="{(1,2) (1,3) (2,3) (3,5) (3,4) (4,2)}"
nums = (input[1:-1])
vec = nums.split(" ")
G = nx.Graph()
fgraph = startUp(vec)
print(fgraph)

Q=[]
A=[]
Q.insert(0,1)

BFS(Q,A,fgraph)


nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

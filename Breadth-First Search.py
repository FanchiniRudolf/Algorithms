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
    iterNum=0
    while(Q):

        print("Iteracion: " + str(iterNum))
        iterNum+=1
        print("Fila Q: "+ str(Q))

        iterator = Q.pop()
        if (iterator not in A):
            A.append(iterator)
        print("Ya visitados: " + str(A))
        tempFile = graph[iterator]
        for item in tempFile:
            if (item not in A):
                Q.insert(0, item)
                A.append(item)
    print("Iteracion: " + str(iterNum))
    print("Fila Q: " + str(Q))
    print("Ya visitados: " + str(A))



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


input=input("Ejemplo: {(1,2) (1,3) (1,4) (2,3) (2,5) (2,6) (3,7) (3,8) (4,8) (7,9)} \n Ponga el suyo: ")
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

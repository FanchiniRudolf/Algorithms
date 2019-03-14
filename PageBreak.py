from tkinter import *
from tkinter import filedialog


# regresa matriz con matrices por renglones
def openArchive(nombre):
    # abrir archivo
    archivo = open(nombre, "r")

    # leer el contenido del archivo
    legend = archivo.read()

    # separar renglones
    vectores = legend.split(" ")

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

            if (nodeVal in graph):
                tempMat = graph[nodeVal]
                tempMat.append(nodePoint)
                graph[nodeVal] = tempMat

            else:
                graph[nodeVal] = [nodePoint]

    archivo.close()
    return graph

def pageRank(graph, rankList):
    for node in range(1,len(graph)+1):
        tempRank = 0
        for pointingNode in range(1, len(graph)+1):
            if(node in graph[pointingNode]):
                tempRank += rankList[pointingNode-1]/len(graph[pointingNode])
        rankList[node-1] = tempRank

    return rankList

graph = openArchive("vec.txt")
rankList = [1/len(graph) for i in range(len(graph))]
print(pageRank(graph, rankList))
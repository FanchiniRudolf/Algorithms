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
    tempList = []
    for x in rankList:
        tempList.append(x)
    for node in graph:
        tempRank = 0.0
        for pointingNode in graph:
            if(node in graph[pointingNode]):
                tempRank += tempList[pointingNode-1]/len(graph[pointingNode])
        rankList[node-1] = tempRank

    return rankList

def getFileName():
    file = filedialog.askopenfile()
    global txtdri1
    txtdri1 = str(file.name)
    dir1.configure(text=txtdri1)
    graph = openArchive(txtdri1)

    iter = int(iterEntry1.get())

    rankList = [1 / len(graph) for i in range(len(graph))]
    for i in range(iter):
        rankList = (pageRank(graph, rankList))

    finalval = "["
    for rank in rankList:
        finalval += " " + str(round(rank, 4)) + ","
    finalval = finalval[:-1]
    finalval += "]"
    resultLabel.configure(text=finalval)

def setFileName():
    input=vectorEntry.get()
    graph={}
    # separar renglones
    vectores = input.split(" ")

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

    iter = int(iterEntry2.get())

    rankList = [1 / len(graph) for i in range(len(graph))]
    for i in range(iter):
        rankList =(pageRank(graph, rankList))

    finalval= "["
    for rank in rankList:
        finalval += " " + str(round(rank, 4)) + ","
    finalval=finalval[:-1]
    finalval+="]"
    resultLabel.configure(text=finalval)


txtdri1 = "No ha escogido ningun archivo"

root = Tk()
root.title("Page Break")
root.geometry("500x300")

topFrame = Frame(root)
topFrame["pady"] = 10
topFrame.pack(side = TOP)

middleFrame = Frame(root)
middleFrame["pady"] = 10
middleFrame.pack(side = TOP)

bottomFrame = Frame(root)
bottomFrame["pady"] = 5
bottomFrame.pack(side=BOTTOM)


accion = Label(topFrame, text="Escoja las direcciones")
accion.pack(side=TOP)

iterLabel1=Label(topFrame, text="Iteracion[#]")
iterEntry1 =Entry(topFrame)
dir1= Label(topFrame, text=txtdri1)
btdir1 = Button(topFrame, text="Escoga archivo", command=getFileName)

iterLabel1.pack(side=TOP)
iterEntry1.pack(side=TOP)
dir1.pack(side=LEFT)
btdir1.pack(side=BOTTOM)

resultLabel = Label(middleFrame, text="Vector ejemplo: (1,2) (2,1) (3,1)")
resultLabel.pack(side=BOTTOM)

inputLabel=Label(bottomFrame, text="Vector:")
vectorEntry = Entry(bottomFrame)
iterLabel2=Label(bottomFrame, text="Iteracion[#]")
iterEntry2 =Entry(bottomFrame)
btEnrty = Button(bottomFrame, text= "Ingrese Texto", command=setFileName)
inputLabel.pack(side=TOP)
vectorEntry.pack(side=TOP)
iterLabel2.pack(side=TOP)
iterEntry2.pack(side=TOP)
btEnrty.pack(side=BOTTOM)



root.mainloop()


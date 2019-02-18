
#regresa matriz con matrices por renglones
def openArchive(nombre):
    #abrir archivo
    archivo = open(nombre, "r",)

    #leer el contenido del archivo
    legend = archivo.read()

    #separar renglones
    renglones = legend.split("\n")


    matriz =[]

    #hacer los renglones arrays de int
    for x in renglones:
        #checar que no este vacio
        if(x==""):
            renglones.remove(x)
        else:
            #separar valores y hacerlos int
            temp = []
            temp = x.split(",")
            for i in range(len(temp)):
                temp[i]= int(temp[i])
            #agregarlos a la matriz
            matriz.append(temp)


    archivo.close()
    return matriz

def fuerzaBruta(matrizA, matrizB):
    matrizC=[]
    dimension = len(matrizA[0])

    for renglones in range(dimension):
        temp=[]
        for i in range(dimension):
            celda=0
            for j in range(dimension):
                celda += matrizA[i][j]*matrizB[j][i]
            temp.append(celda)
        matrizC.append(temp)

    return matrizC

matrizA = openArchive("3x3A.txt")
matrizB = openArchive("3x3B.txt")
print(fuerzaBruta(matrizA, matrizB))





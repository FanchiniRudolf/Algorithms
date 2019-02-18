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


print(openArchive("01. Matrix_A_16_2_4.txt"))
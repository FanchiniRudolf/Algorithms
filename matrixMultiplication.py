
def openArchive(nombre):
    archivo1 = open(nombre, "r",)

    legend = archivo1.read()

    renglones = legend.split("\n")

    matriz =[]
    for x in renglones:
        if(x==""):
            renglones.remove(x)
        else:
            temp = []
            temp = x.split(",")
            for i in range(len(temp)):
                temp[i]= int(temp[i])
            matriz.append(temp)


    archivo1.close()

    return matriz


print(openArchive("01. Matrix_A_16_2_4.txt"))


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
    l1 = len(matrizA[0])*len(matrizA);
    l2 = len(matrizA[0]);

    indiceFila = 0;
  
    numerosAgregados = 0;
    matrizC = [];

    while(len(matrizC)<l2):
        matrizC.append([]);
    currentFilaMC = 0;
    auxiliar = 0;

    while numerosAgregados < l1:
        calculado = 0;

        contadorElementosColumna = 0;
        currentFila = matrizA[indiceFila];
        indiceColumna = auxiliar;
        for elemento in currentFila:
            calculado = calculado + (elemento*matrizB[contadorElementosColumna][indiceColumna]);
            contadorElementosColumna += 1;


        matrizC[currentFilaMC].append(calculado);
        numerosAgregados+=1;
        auxiliar+=1;


        if(auxiliar==len(currentFila)):
            auxiliar=0;
            indiceFila+=1;
            currentFilaMC += 1;

    return matrizC


matrizA = openArchive("01. Matrix_A_16_2_4.txt")
matrizB = openArchive("02. Matrix_B_16_2_4.txt")
print(fuerzaBruta(matrizA, matrizB))


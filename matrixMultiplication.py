
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


<<<<<<< HEAD




matrizA = openArchive("01. Matrix_A_16_2_4.txt")
matrizB = openArchive("02. Matrix_B_16_2_4.txt")
print(fuerzaBruta(matrizA, matrizB))
=======
def strassen(matrizA, matrizB):
    n = len(matrizA[0])
    matrizC=[]

    matrizA11 = []
    matrizA12 = []
    matrizA21 = []
    matrizA22 = []

    matrizB11 = []
    matrizB12 = []
    matrizB21 = []
    matrizB22 = []

    if (n==2):
        #hacemos caso base
        print("hola que hace")
    else:
        print(matrizB[3][3])
        for i in range(n):
            for j in range(n):
                if (i <n/2 and j<n/2 ):
                    #se van a a11 b11
                    matrizA11.append(matrizA[i][j])
                    matrizB11.append(matrizB[i][j])
                elif (i>=n/2 and j<n/2 ):
                    #se van a a12 b12
                    matrizA12.append(matrizA[i][j])
                    matrizB12.append(matrizB[i][j])
                elif (i<n/2 and j>=n/2 ):
                    #se van a a21 b21
                    matrizA21.append(matrizA[i][j])
                    matrizB21.append(matrizB[i][j])
                elif (i>=n/2 and j>=n/2 ):
                    # se van a a22 b22
                    matrizA22.append(matrizA[i][j])
                    matrizB22.append(matrizB[i][j])

    print(matrizA11)
    print(matrizA12)
    print(matrizA21)
    print(matrizA22)
    print(matrizB11)
    print(matrizB12)
    print(matrizB21)
    print(matrizB22)

    return matrizC


#dir1= input("Deme la dirección de la primera matriz")

matrizA = openArchive("3X3A.txt")
matrizB = openArchive("3x3B.txt")
strassen(matrizA, matrizB)

>>>>>>> 3f33eb6a8c42d0919c39a030b4f4e3c7cc26ae5b

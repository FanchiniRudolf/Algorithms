
# regresa matriz con matrices por renglones
def openArchive(nombre):
    # abrir archivo
    archivo = open(nombre, "r")

    # leer el contenido del archivo
    legend = archivo.read()

    # separar renglones
    renglones = legend.split("\n")

    matriz = []

    # hacer los renglones arrays de int
    for x in renglones:
        # checar que no este vacio
        if (x == ""):
            renglones.remove(x)
        else:
            # separar valores y hacerlos int
            temp = []
            temp = x.split(",")
            for i in range(len(temp)):
                temp[i] = int(temp[i])
            # agregarlos a la matriz
            matriz.append(temp)

    archivo.close()
    return matriz


def fuerzaBruta(matrizA, matrizB):
    len1 = len(matrizA[0]) * len(matrizA);
    len2 = len(matrizA[0]);
    contadorMultiplicaciones = 0;

    indiceFila = 0;

    numerosAgregados = 0;
    matrizC = [];

    while (len(matrizC) < len2):
        matrizC.append([]);
    currentFilaMC = 0;
    auxiliar = 0;

    while numerosAgregados < len1:
        calculado = 0;
        contadorElementosColumna = 0;
        currentFila = matrizA[indiceFila];
        indiceColumna = auxiliar;
        for elemento in currentFila:
            calculado = calculado + (elemento * matrizB[contadorElementosColumna][indiceColumna]);
            contadorElementosColumna += 1;
            contadorMultiplicaciones +=1;

        matrizC[currentFilaMC].append(calculado);
        numerosAgregados += 1;
        auxiliar += 1;

        if (auxiliar == len(currentFila)):
            auxiliar = 0;
            indiceFila += 1;
            currentFilaMC += 1;

    print(contadorMultiplicaciones);
    return matrizC


def restaMatriz(matrizA, matrizB):
    matrizC = []
    for k in range(len(matrizA)):
        matrizC.append([])
    for i in range(len(matrizA)):
        for j in range(len(matrizA[0])):
            matrizC[i].append(matrizA[i][j] - matrizB[i][j])
    return matrizC


def sumaMatriz(matrizA, matrizB):
    matrizC = []
    for k in range(len(matrizA)):
        matrizC.append([])
    for i in range(len(matrizA)):
        for j in range(len(matrizA[0])):
            matrizC[i].append(matrizA[i][j] + matrizB[i][j])
    return matrizC


def strassen(matrizA, matrizB):
    n = len(matrizA[0]);
    global multis


    if (n <= 2):
        multis+=8;
        return fuerzaBruta(matrizA, matrizB);


    else:
        matrizC = [[0 for i in range(n)] for j in range(n)];
        A11 = [];
        A12 = [];
        A21 = [];
        A22 = [];
        B11 = [];
        B12 = [];
        B21 = [];
        B22 = [];

        lenABs = n / 2;
        for i in range(int(lenABs)):
            A11.append([]);
            A12.append([]);
            A21.append([]);
            A22.append([]);
            B11.append([]);
            B12.append([]);
            B21.append([]);
            B22.append([]);

        for i in range(len(matrizA)):
            currentFilaA = matrizA[i];
            currentFilaB = matrizB[i];

            for j in range(len(currentFilaA)):
                auxiliarI = i;
                lenA = len(matrizA);
                if (i >= lenA / 2):
                    auxiliarI -= int((lenA / 2));
                elementoA = currentFilaA[j];
                elementoB = currentFilaB[j];
                if (i < lenA / 2 and j < len(currentFilaA) / 2):
                    A11[auxiliarI].append(elementoA);
                    B11[auxiliarI].append(elementoB);
                elif (i < lenA / 2 and j >= len(currentFilaA) / 2):
                    A12[auxiliarI].append(elementoA);
                    B12[auxiliarI].append(elementoB);
                elif (i >= lenA / 2 and j < len(currentFilaA) / 2):
                    A21[auxiliarI].append(elementoA);
                    B21[auxiliarI].append(elementoB);
                else:
                    A22[auxiliarI].append(elementoA);
                    B22[auxiliarI].append(elementoB);
        m1 = strassen(sumaMatriz(A11, A22), sumaMatriz(B11, B22));
        m2 = strassen(sumaMatriz(A21, A22), B11);
        m3 = strassen(A11, restaMatriz(B12, B22));
        m4 = strassen(A22, restaMatriz(B21, B11));
        m5 = strassen(sumaMatriz(A11, A12), B22);
        m6 = strassen(restaMatriz(A21, A11), sumaMatriz(B11, B12));
        m7 = strassen(restaMatriz(A12, A22), sumaMatriz(B21, B22));

        C11 = sumaMatriz(m1, m4);
        C11 = restaMatriz(C11, m5);
        C11 = sumaMatriz(C11, m7);
        C12 = sumaMatriz(m3, m5);
        C21 = sumaMatriz(m2, m4);
        C22 = sumaMatriz(m1, m3);
        C22 = restaMatriz(C22, m2);
        C22 = sumaMatriz(C22, m6);

        for i in range(n // 2):
            for j in range(n // 2):
                matrizC[i][j] = C11[i][j]
                matrizC[i][j + n // 2] = C12[i][j]
                matrizC[i + n // 2][j] = C21[i][j]
                matrizC[i + n // 2][j + n // 2] = C22[i][j]

        return matrizC;

multis = 0;
matrizA = openArchive("01. Matrix_A_16_2_4.txt")
matrizB = openArchive("02. Matrix_B_16_2_4.txt")
print(fuerzaBruta(matrizA, matrizB));
print(strassen(matrizA, matrizB));
print(multis);
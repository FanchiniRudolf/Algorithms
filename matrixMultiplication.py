import sys


# regresa matriz con matrices por renglones
def openArchive(nombre):
    # abrir archivo
    archivo = open(nombre, "r", )

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

        matrizC[currentFilaMC].append(calculado);
        numerosAgregados += 1;
        auxiliar += 1;

        if (auxiliar == len(currentFila)):
            auxiliar = 0;
            indiceFila += 1;
            currentFilaMC += 1;

    return matrizC


def strassen(matrizA, matrizB):
    n = len(matrizA)
    matrizC = [[0 for i in range(n)] for j in range(n)]

    matrizA11 = [[0 for i in range(int(n / 2))] for j in range(int(n / 2))]
    matrizA12 = [[0 for i in range(int(n / 2))] for j in range(int(n / 2))]
    matrizA21 = [[0 for i in range(int(n / 2))] for j in range(int(n / 2))]
    matrizA22 = [[0 for i in range(int(n / 2))] for j in range(int(n / 2))]

    matrizB11 = [[0 for i in range(int(n / 2))] for j in range(int(n / 2))]
    matrizB12 = [[0 for i in range(int(n / 2))] for j in range(int(n / 2))]
    matrizB21 = [[0 for i in range(int(n / 2))] for j in range(int(n / 2))]
    matrizB22 = [[0 for i in range(int(n / 2))] for j in range(int(n / 2))]

    if (n == 2):
        # hacemos caso base
        A11 = matrizA[0][0]
        A12 = matrizA[0][1]
        A21 = matrizA[1][0]
        A22 = matrizA[1][1]

        B11 = matrizB[0][0]
        B12 = matrizB[0][1]
        B21 = matrizB[1][0]
        B22 = matrizB[1][1]

        m1 = (A11 + A22) * (B11 + B22)
        m2 = (A21 + A22) * B11
        m3 = A11 * (B12 - B22)
        m4 = A22 * (B21 - B11)
        m5 = (A11 + A12) * B22
        m6 = (A21 - A11) * (B11 + B12)
        m7 = (A12 - A22) * (B21 + B22)

        matrizC = [[m1 + m4 - m5 + m7, m3 + m5], [m2 + m4, m1 + m3 - m2 + m6]]

    else:
        for i in range(n // 2):
            for j in range(n // 2):
                # asignar valores de la grande a la chica
                matrizA11[i][j] = matrizA[i][j]
                matrizA12[i][j] = matrizA[i][j + n // 2]
                matrizA21[i][j] = matrizA[i + n // 2][j]
                matrizA22[i][j] = matrizA[i + n // 2][j + n // 2]

                matrizB11[i][j] = matrizB[i][j]
                matrizB12[i][j] = matrizB[i][j + n // 2]
                matrizB21[i][j] = matrizB[i + n // 2][j]
                matrizB22[i][j] = matrizB[i + n // 2][j + n // 2]

        m1 = strassen(sumaMatriz(matrizA11, matrizA22), sumaMatriz(matrizB11, matrizB22))
        m2 = strassen(sumaMatriz(matrizA21, matrizA22), matrizB11)
        m3 = strassen(matrizA11, restaMatriz(matrizB12, matrizB22))
        m4 = strassen(matrizA22, restaMatriz(matrizB21, matrizB11))
        m5 = strassen(sumaMatriz(matrizA11, matrizA12), matrizB22)
        m6 = strassen(restaMatriz(matrizA21, matrizA11), sumaMatriz(matrizB11, matrizB12))
        m7 = strassen(restaMatriz(matrizA12, matrizA22), sumaMatriz(matrizB21, matrizB22))

        matrizC11 = restaMatriz(sumaMatriz(m1, m4), sumaMatriz(m5, m7))
        matrizC12 = sumaMatriz(m3, m5)
        matrizC21 = sumaMatriz(m2, m4)
        matrizC22 = restaMatriz(sumaMatriz(m1, m3), sumaMatriz(m2, m6))

        for i in range(n // 2):
            for j in range(n // 2):
                matrizC[i][j] = matrizC11[i][j]
                matrizC[i][j + n // 2] = matrizC12[i][j]
                matrizC[i + n // 2][j] = matrizC21[i][j]
                matrizC[i + n // 2][j + n // 2] = matrizC22[i][j]

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

def strassen2(matrizA, matrizB):
    n = len(matrizA[0]);

    if(n<=2):
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

    lenABs = n/2;
    for i in range(lenABs):
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

        for j in range (len(currentFilaA)):
            auxiliarI = i;
            lenA = len(matrizA);
            if (i >= lenA / 2):
                auxiliarI -= (lenA / 2);
            elementoA = currentFilaA[j];
            elementoB =  currentFilaB[j];
            if(i < lenA/2 and j < len(currentFilaA)/2):
                A11[auxiliarI].append (elementoA);
                B11[auxiliarI].append(elementoB);
            elif(i < lenA/2 and j >= len(currentFilaA)/2):
                A12[auxiliarI].append(elementoA);
                B12[auxiliarI].append(elementoB);
            elif(i >= lenA/2 and j < len(currentFilaA)/2):
                A21[auxiliarI].append(elementoA);
                B21[auxiliarI].append(elementoB);
            else:
                A22[auxiliarI].append(elementoA);
                B22[auxiliarI].append(elementoB);
    m1 = strassen2(sumaMatriz(A11, A22), sumaMatriz(B11, B22));
    m2 = strassen2(sumaMatriz(A21, A22), B11);
    m3 = strassen2(A11, restaMatriz(B12, B22));
    m4 = strassen2(A22, restaMatriz(B21, B11));
    m5 = strassen2(sumaMatriz(A11, A12), B22);
    m6 = strassen2(restaMatriz(A21, A11), sumaMatriz(B11, B12));
    m7 = strassen2(restaMatriz(A12, A22), sumaMatriz(B21, B22));

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





matrizA = openArchive("01. Matrix_A_16_2_4.txt")
matrizB = openArchive("02. Matrix_B_16_2_4.txt")
matrizC = openArchive("matriz3.txt");
matrizD = openArchive("matriz32.txt");
print(strassen2(matrizA, matrizB))
print(strassen2(matrizA, matrizB)==fuerzaBruta(matrizA, matrizB))


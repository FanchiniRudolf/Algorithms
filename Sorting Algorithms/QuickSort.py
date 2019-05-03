#Rudolf Josef Fanchini Reyes A01374448
#Eduardo Gallegos Solís A01745776

# regresa matriz con matrices
def openArchive(nombre):
    # abrir archivo
    archivo = open(nombre, "r")

    # leer el contenido del archivo
    legend = archivo.read()

    matriz = legend.split(",")
    for x in range(0, len(matriz)):
        matriz[x] = int(matriz[x])

    archivo.close()
    return matriz

def QuickSort(values, start, end):
    if(start>=end):
        return
    divider = values[start]

    lo = start
    hi = end
    while(True):
        while(values[hi]>=divider):
            hi = hi -1
            if (hi<= lo):
                break
        if (hi<=lo):
            values[lo]=divider
        values[lo] = values[hi]
        lo = lo +1
        while(values[lo]<divider):
            lo = lo + 1
            if (lo >= hi):
                break
        if (lo >= hi):
            lo = hi
            values[hi] = divider
            break
        values[hi] = values[lo]
    QuickSort(values, start, lo-1)
    QuickSort(values, lo+1, end)



array = openArchive("numbers.txt")
print(array)
QuickSort(array,0,len(array)-1)
print(array)



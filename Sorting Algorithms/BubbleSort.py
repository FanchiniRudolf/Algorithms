"""Bubblesort(Data: values[])
// Repeat until the array is sorted.
Boolean: not_sorted = True
While (not_sorted)
// Assume we won't find a pair to swap.
not_sorted = False
// Search the array for adjacent items that are out of order.
For i = 0 To <length of values> - 1
// See if items i and i - 1 are out of order.
If (values[i] < values[i - 1]) Then
// Swap them.
Data: temp = values[i]
values[i] = values[i - 1]
values[i - 1] = temp
// The array isn't sorted after all.
not_sorted = True
End If
Next i
End While
End Bubblesort
"""

def bubbleSort(lista):
    notSorted = True

    while(notSorted):
        notSorted = False
        for i in range(1, len(lista)):
            if(int(lista[i])<int(lista[i-1])):
                temp = lista[i]
                lista[i] = lista[i-1]
                lista[i-1] = temp
                notSorted = True

archivo = open("numbers.txt", "r")
numeros = archivo.readlines()
archivo.close()
arr = []
for i in range(0, len(numeros)):
    num = numeros[i].split(",")
    num[len(num) - 1] = num[len(num) - 1].replace("\n", "")
    for y in range(0, len(num)):
        arr.append(int(num[y]))
bubbleSort(arr)
print(arr)
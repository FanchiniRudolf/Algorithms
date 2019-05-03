#Rudolf Josef Fanchini Reyes A01374448
#Eduardo Gallegos Solís A01745776

import math

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

def counting_sort(A, digit, radix):
    #"A" is a list to be sorted, radix is the base of the number system, digit is the digit
    #we want to sort by

    #create a list B which will be the sorted list
    B = [0]*len(A)
    C = [0]*int(radix)
    #counts the number of occurences of each digit in A
    for i in range(0, len(A)):
        digit_of_Ai = int((A[i]/radix**digit)%radix)
        C[digit_of_Ai] = C[digit_of_Ai] +1
        #now C[i] is the value of the number of elements in A equal to i

    #this FOR loop changes C to show the cumulative # of digits up to that index of C
    for j in range(1,radix):
        C[j] = C[j] + C[j-1]
        #here C is modifed to have the number of elements <= i
    for m in range(len(A)-1, -1, -1): #to count down (go through A backwards)
        digit_of_Ai = int((A[m]/radix**digit)%radix)
        C[digit_of_Ai] = C[digit_of_Ai] -1
        B[C[digit_of_Ai]] = A[m]

    return B

#alist = [9,3,1,4,5,7,7,2,2]
#print countingSort(alist,0,10)

def radix_sort(A, radix):
    #radix is the base of the number system
    #k is the largest number in the list
    k = max(A)
    #output is the result list we will build
    output = A
    #compute the number of digits needed to represent k
    digits = int(math.floor(math.log(k, radix)+1))
    for i in range(digits):
        output = counting_sort(output,i,radix)

    return output

#A = [9,3,1,4,5,7,7,2,20,55]
A = openArchive("numbers.txt")
positive = []
negative = []
for number in A:
    if (number<0):
        negative.append(number)
    else:
        positive.append(number)

temp =min(negative)
negative.append(temp*-1)
positive = (radix_sort(positive,10))
negative = radix_sort(negative, 10)
A = negative + positive
A = A[1::]
print(A)



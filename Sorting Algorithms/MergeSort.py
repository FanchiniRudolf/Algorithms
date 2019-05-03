"""Mergesort(Data: values[], Data: scratch[], Integer: start, Integer: end)
// If the array contains only one item, it is already sorted.
If (start == end) Then Return
// Break the array into left and right halves.
Integer: midpoint = (start + end) / 2
// Call Mergesort to sort the two halves.
Mergesort(values, scratch, start, midpoint)
Mergesort(values, scratch, midpoint + 1, end)
// Merge the two sorted halves.
Integer: left_index = start
Integer: right_index = midpoint + 1
Integer: scratch_index = left_index
While ((left_index <= midpoint) And (right_index <= end))
If (values[left_index] <= values[right_index]) Then
scratch[scratch_index] = values[left_index]
left_index = left_index + 1
Else
scratch[scratch_index] = values[right_index]
right_index = right_index + 1
End If
scratch_index = scratch_index + 1 End While
// Finish copying whichever half is not empty.
For i = left_index To midpoint
scratch[scratch_index] = values[i]
scratch_index = scratch_index + 1
Next i
For i = right_index To end
scratch[scratch_index] = values[i]
scratch_index = scratch_index + 1
Next i
// Copy the values back into the original values array.
For i = start To end
values[i] = scratch[i]
Next i
End Mergesort
"""

#Rudolf Josef Fanchini Reyes A01374448
#Eduardo Gallegos Solís A01745776

def mergeSort(alist):


   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1


archivo = open("numbers.txt", "r")
numeros = archivo.readlines()
archivo.close()
arr = []
for i in range(0, len(numeros)):
    num = numeros[i].split(",")
    num[len(num) - 1] = num[len(num) - 1].replace("\n", "")
    for y in range(0, len(num)):
        arr.append(int(num[y]))
mergeSort(arr)
print(arr)
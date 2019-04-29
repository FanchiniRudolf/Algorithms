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
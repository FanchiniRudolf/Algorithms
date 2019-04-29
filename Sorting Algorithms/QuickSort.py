"""// Sort the indicated part of the array.
Quicksort(Data: values[], Integer: start, Integer: end)
// If the list has no more than one element, it's sorted.
If (start >= end) Then Return
// Use the first item as the dividing item.
Integer: divider = values[start]
// Move items < divider to the front of the array and
// items >= divider to the end of the array.
Integer: lo = start
Integer: hi = end
While (True)
// Search the array from back to front starting at "hi"
// to find the last item where value < "divider."
// Move that item into the hole. The hole is now where
// that item was.
While (values[hi] >= divider)
hi = hi - 1
If (hi <= lo) Then <Break out of the inner While loop.>
End While
If (hi <= lo) Then
// The left and right pieces have met in the middle
// so we're done. Put the divider here, and
// break out of the outer While loop.
values[lo] = divider
<Break out of the outer While loop.>
End If
// Move the value we found to the lower half.
values[lo] = values[hi]
// Search the array from front to back starting at "lo"
// to find the first item where value >= "divider."
// Move that item into the hole. The hole is now where
// that item was.
lo = lo + 1
While (values[lo] < divider)
lo = lo + 1
If (lo >= hi) Then <Break out of the inner While loop.>
End While
If (lo >= hi) Then
// The left and right pieces have met in the middle
// so we're done. Put the divider here, and
// break out of the outer While loop.
lo = hi
values[hi] = divider
<Break out of the outer While loop.>
End If
// Move the value we found to the upper half.
values[hi] = values[lo]
End While
// Recursively sort the two halves.
Quicksort(values, start, lo - 1)
Quicksort(values,lo + 1, end)
End Quicksort
"""
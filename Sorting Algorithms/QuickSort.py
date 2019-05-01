
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



array = [123,983,2,5,76,4,-12,43,-5,53,71,-34]
QuickSort(array,0,len(array)-1)
print(array)



def finbonacciSearch(list,requiredNumber):
    size=len(list)

    initialStart=-1

    m=0
    l=1
    r=1
    while(r<size):
        m=l
        l=r
        r=m+l

    while(r>1):
        idx=min(initialStart+m, size-1)
        if list[idx] < requiredNumber:
            r=l
            l=m
            m=r-l
            initialStart=idx
        elif list[idx] < requiredNumber:
            r=m
            l-=m
            m=r-l
        else:
            return idx

        if l and list[size-1] == requiredNumber:
            return size-1
        return "Wasn't found"

ex = []
print(finbonacciSearch())

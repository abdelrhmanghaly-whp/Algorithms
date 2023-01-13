def binarySearch(list, requiredNumber):
    left = 0 
    right = len(list)-1
    
    while left < right:
        mid = int((left+right)/2)
        check=list[mid]

        if check == requiredNumber:
            return mid
        elif check > requiredNumber:
            right = mid -1
        else:
            left = mid +1

    return "Wasn't found"

ex = []
print(binarySearch())


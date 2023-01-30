def heapSort(list, child, root):
    maximum = root
    left = 2 * root + 1
    right = 2* root + 2
    
    if left < child and list[root] < list[left]:
        maximum = left
    if right < child and list[maximum] < list[right]:
        maximum = right
    if maximum != root:
        (list[root], list[maximum]) = (list[maximum], list[root])
        heapSort(list,child,maximum)

def Sort(list): # max heap
    child = len(list)
    # existed parent at (ch//2-1), perf swap
    for i in range(child // 2-1,-1,-1):
        heapSort(list,child,i)

    for i in range(child-1,0,-1):
        (list[i], list[0]) = (list[0],list[i])
        heapSort(list,i,0)

def display(list):
    Sort(list)
    child = len(list)
    print("The Sorted List is: ")
    for i in range(child):
        print(list[i], end=" ")


list = [4,10,90,1,8,22]
ex = [9,8,7,6,5,4,3,2,1]
display(list)
print("\n")
display(ex)

def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

def mergeSort(nlist):
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1

def heapify(list3, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1    # left = 2*i + 1 
    r = 2 * i + 2    # right = 2*i + 2 

    # See if left child of root exists and is 
    # greater than root 
    if l < n and list3[i] < list3[l]: 
        largest = l 

    # See if right child of root exists and is 
    # greater than root 
    if r < n and list3[largest] < list3[r]: 
        largest = r 

    # Change root, if needed 
    if largest != i: 
        list3[i],list3[largest] = list3[largest],list3[i] # swap 

        # Heapify the root. 
        heapify(list3, n, largest) 

def heapSort(list3): 
    n = len(list3) 

    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(list3, n, i) 

    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        list3[i], list3[0] = list3[0], list3[i] # swap 
        heapify(list3, i, 0) 

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
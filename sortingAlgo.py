import time
from algo import insertionSort, mergeSort, heapSort, heapify 

DataFile = open( 'Data.txt', 'r')
list1 = DataFile.readlines()
list2 = list1
list3=list2
DataFile1 = open( 'multifiles/data3.txt', 'w')
DataFile2 = open( 'multifiles/data3.txt', 'r')

#print(list2)

start_time_merge = time.time()
mergeSort(list1)
print("merge sort :")
#print(list1)
print("--- %s seconds ---" % (time.time() - start_time_merge))


start_time_insertion = time.time()
insertionSort(list2)
print("insertion sort :")
#print(list2)
print("--- %s seconds ---" % (time.time() - start_time_insertion))

start_time_heap = time.time()
heapSort(list3)
print("heap sort :")
#print(list1)
print("--- %s seconds ---" % (time.time() - start_time_heap))


for x in list1:
    DataFile1.write(x)

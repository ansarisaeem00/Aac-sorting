from algo import insertionSort ,mergeSort ,heapify ,heapSort
import time


DataFile = open( 'multifiles/data1.txt', 'r')
list1 = DataFile.readlines()

DataFile = open( 'multifiles/data2.txt', 'r')
list2 = DataFile.readlines()

mergeList = list1 + list2


start_time_merge = time.time()
mergeSort(mergeList)
print("merge sort :")
#print(list1)
print("--- %s seconds ---" % (time.time() - start_time_merge))


start_time_insertion = time.time()
insertionSort(mergeList)
print("insertion sort :")
#print(list2)
print("--- %s seconds ---" % (time.time() - start_time_insertion))

start_time_heap = time.time()
heapSort(mergeList)
print("heap sort :")
#print(list1)
print("--- %s seconds ---" % (time.time() - start_time_heap))

DataFile1 = open( 'Iteration0/data1.txt', 'w')
for x in mergeList:
	DataFile1.write(x)
import random
from algo import insertionSort ,mergeSort ,heapify ,heapSort, read_integers
import time

list2 = list3 = list1 = read_integers("Data.txt")

start_time_merge = time.time()
mergeSort(list1)
timemerge = (time.time() - start_time_merge)
print("merge sort :")
print("--- %s mili seconds ---" % timemerge)

start_time_insertion = time.time()
insertionSort(list2)
timeinsert = (time.time() - start_time_merge)		
print("insertion sort :")
#print(list2)
print("--- %s mili seconds ---" % timeinsert)

start_time_heap = time.time()
heapSort(list3)
timeheap = (time.time() - start_time_heap)
print("heap sort :")
#print(list1)
print("--- %s mili seconds ---" % timeheap)
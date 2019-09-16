import random
from algo import insertionSort ,mergeSort ,heapify ,heapSort, read_integers
import time
import pandas as pd


#---------Some Constant Declaration
noOfTotalRnadomElement = 800000 
startReading = 0 
endReading = 50000
increaseRate = 50000
noOfFiles = int(noOfTotalRnadomElement/increaseRate)
totalTimeMerge = 0
totalTimeInsertion = 0
totalTimeheap = 0
inserttimelist=[]
mergetimelist=[]
heaptimelist=[]
blank = [""]
analyse = open("Analyse.txt", 'w')
#print(type(noOfFiles))
#Generating No
print("-----------Generating " + str(noOfTotalRnadomElement) + " Random no-----------")
f = open( 'Data.txt', 'w') #write data file 
for x in range(noOfTotalRnadomElement): #generate random no
	f.write( repr(random.randint(1,4000)) + '\n')
f.close()
print("-----------Successfully generated " + str(noOfTotalRnadomElement) + " Random no-----------")


#reading data file
DataFile = open( 'Data.txt', 'r')
lines = DataFile.readlines()


#------Genrating Files
print("-----------Generating files contains " + str(increaseRate) + " Random no-----------")
for i in range(1,noOfFiles+1):
	file_name ="randomFiles/data" + str(i) + ".txt" #file name at each iteration 
	startReading = 0 
	endReading = 50000
	#print("data" + str(i) + ".txt")
	#both reading are nothing but line no	
	fz = open(file_name , 'w')
	for x in lines[startReading:endReading]:
		fz.write(x)
	fz.close()	
	startReading = startReading + endReading + 1
	endReading = endReading + increaseRate

print("-----------Successfully created " + str(noOfFiles) +  " files-----------")
DataFile.close()



#------Sorting
print("-----------Sorting Each  " + str(noOfFiles) +  " files-----------")
for i in range(1,noOfFiles+1):
	file_name = "randomFiles/data" + str(i) + ".txt"
	file_name_write = "sortedFiles/data" + str(i) + ".txt"
	print("----file" + str(i) + "----")
	list1 = read_integers(file_name)
	list3 = list2 = list1 
	DataFileWrite = open( file_name_write, 'w')

	start_time_merge = time.time()
	mergeSort(list1)
	timemerge = (time.time() - start_time_merge)
	totalTimeMerge = totalTimeMerge + timemerge
	print("merge sort :")
	print("--- %s mili seconds ---" % timemerge)
	mergetimelist.append(timemerge)

	start_time_insertion = time.time()
	insertionSort(list2)
	timeinsert = (time.time() - start_time_merge)
	totalTimeInsertion = totalTimeInsertion + timeinsert		
	print("insertion sort :")
	#print(list2)
	print("--- %s mili seconds ---" % timeinsert)
	inserttimelist.append(timeinsert)

	start_time_heap = time.time()
	heapSort(list3)
	timeheap = (time.time() - start_time_heap)
	totalTimeheap = totalTimeheap + timeheap	
	print("heap sort :")
	#print(list1)
	print("--- %s mili seconds ---" % timeheap)
	heaptimelist.append(timeheap)
	for x in list1:
		DataFileWrite.write(str(x)+"\n")

print("-----------Successfully Sorted Each  " + str(noOfFiles) +  " files-----------")

merge50 = []
heap50 = []
insert50 = []

merge50 = mergetimelist
heap50 = heaptimelist
insert50 = inserttimelist

mergetimelist=[]
heaptimelist=[]
inserttimelist=[]


print("-----------Merging Each  " + str(noOfFiles) +  " files (iteration-0)-----------")
#-------Merging iteration-0
for i in range(1,(noOfFiles+1)):
	if i% 2 != 0:
		file1 = "sortedFiles/data" + str(i) + ".txt"
		j = i+1
		file2 = "sortedFiles/data" + str(j) + ".txt"
		list1 = read_integers(file1)
		list2 = read_integers(file2)
		mergeList3 = mergeList2 = mergeList1 = list1 + list2

		start_time_merge = time.time()
		mergeSort(mergeList1)
		timemerge = (time.time() - start_time_merge)
		totalTimeMerge = totalTimeMerge + timemerge
		print("merge sort :")
		#print(list1)
		print("--- %s seconds ---" % timemerge)
		mergetimelist.append(timemerge)


		start_time_insertion = time.time()
		insertionSort(mergeList2)
		timeinsert = (time.time() - start_time_merge)
		totalTimeInsertion = totalTimeInsertion + timeinsert
		print("insertion sort :")
		#print(list2)
		print("--- %s seconds ---" % timeinsert)
		inserttimelist.append(timeinsert)


		start_time_heap = time.time()
		heapSort(mergeList3)
		timeheap = (time.time() - start_time_heap)
		totalTimeheap = totalTimeheap + timeheap	
		print("heap sort :")
		#print(list1)
		print("--- %s seconds ---" % timeheap)
		heaptimelist.append(timeheap)

		mergeFileName ="Iteration0/data" + str(i) + str(j) + ".txt" 
		print("-----------Creating file  " + str(mergeFileName) +  "-----------")
		mergeFile = open( mergeFileName, 'w')
		for x in mergeList1:
			mergeFile.write(str(x)+"\n")
print("-----------Successfully Merge Each  " + str(noOfFiles) +  " files into " + str(noOfFiles/2) +"(iteration-0)-----------")

merge100 = []
heap100 = []
insert100 = []

merge100 = mergetimelist + blank*8
heap100 = heaptimelist + blank*8
insert100 = inserttimelist + blank*8


mergetimelist=[]
heaptimelist=[]
inserttimelist=[]



print("-----------Merging Each  " + str(noOfFiles/2) +  " files (iteration-1)-----------")
#noOfFilesIteration1 = noOfFiles/2
#-------Merging iteration-1
for i in range(1,16,4):
	x = i
	y = j = i+1
	file1 = "Iteration0/data" + str(i) + str(j) + ".txt"		
	i = i+2
	j = i+1
	file2 = "Iteration0/data" +  str(i) + str(j) + ".txt"
	list1 = read_integers(file1)
	list2 = read_integers(file2)
	mergeList3 = mergeList2 = mergeList1 = list1 + list2

	start_time_merge = time.time()
	mergeSort(mergeList1)
	timemerge = (time.time() - start_time_merge)
	totalTimeMerge = totalTimeMerge + timemerge
	print("merge sort :")
	#print(list1)
	print("--- %s seconds ---" % timemerge)
	mergetimelist.append(timemerge)

	start_time_insertion = time.time()
	insertionSort(mergeList2)
	timeinsert = (time.time() - start_time_merge)
	totalTimeInsertion = totalTimeInsertion + timeinsert
	print("insertion sort :")
	#print(list2)
	print("--- %s seconds ---" % timeinsert)
	inserttimelist.append(timeinsert)


	start_time_heap = time.time()
	heapSort(mergeList3)
	timeheap = (time.time() - start_time_heap)
	totalTimeheap = totalTimeheap + timeheap	
	print("heap sort :")
	#print(list1)
	print("--- %s seconds ---" % timeheap)
	heaptimelist.append(timeheap)

	mergeFileName ="Iteration1/data" + str(x) + str(y) + str(i) + str(j) + ".txt" 
	print("-----------Creating file  " + str(mergeFileName) +  "-----------")
	mergeFile = open( mergeFileName, 'w')
	for x in mergeList1:
		mergeFile.write(str(x)+"\n")
print("-----------Successfully Merge Each  " + str(noOfFiles/2) +  " files into " + str(noOfFiles/4) +"(iteration-1)-----------")


merge200 = []
heap200 = []
insert200 = []

merge200 = mergetimelist + blank*12
heap200 = heaptimelist + blank*12
insert200 = inserttimelist + blank*12

mergetimelist=[]
heaptimelist=[]
inserttimelist=[]


print("-----------Merging Each  " + str(noOfFiles/4) +  " files (iteration-2)-----------")
#noOfFilesIteration1 = noOfFiles/2
#-------Merging iteration-2
for i in range(1,16,8):
	x = i+1
	y = x+1
	j = y+1
	p1 = str(i) + str(x) + str(y) + str(j)
	file1 = "Iteration1/data" + str(p1) + ".txt"		
	i = j+1
	x = i+1
	y = x+1
	j = y+1
	p2 = str(i) + str(x) + str(y) + str(j)
	file2 = "Iteration1/data" +  str(p2)+ ".txt"
	list1 = read_integers(file1)
	list2 = read_integers(file2)
	mergeList3 = mergeList2 = mergeList1  = list1 + list2

	start_time_merge = time.time()
	mergeSort(mergeList1)
	timemerge = (time.time() - start_time_merge)
	totalTimeMerge = totalTimeMerge + timemerge
	print("merge sort :")
	#print(list1)
	print("--- %s seconds ---" % timemerge)
	mergetimelist.append(timemerge)

	start_time_insertion = time.time()
	insertionSort(mergeList2)
	timeinsert = (time.time() - start_time_merge)
	totalTimeInsertion = totalTimeInsertion + timeinsert
	print("insertion sort :")
	#print(list2)
	print("--- %s seconds ---" % timeinsert)
	inserttimelist.append(timeinsert)


	start_time_heap = time.time()
	heapSort(mergeList3)
	timeheap = (time.time() - start_time_heap)
	totalTimeheap = totalTimeheap + timeheap	
	print("heap sort :")
	#print(list1)
	print("--- %s seconds ---" % timeheap)
	heaptimelist.append(timeheap)

	mergeFileName ="Iteration2/data" + str(p1) + str(p2) + ".txt" 
	print("-----------Creating file  " + str(mergeFileName) +  "-----------")
	mergeFile = open( mergeFileName, 'w')
	for x in mergeList1:
		mergeFile.write(str(x)+"\n")
print("-----------Successfully Merge Each  " + str(noOfFiles/4) +  " files into " + str(noOfFiles/8) +"(iteration-2)-----------")


merge400 = []
heap400 = []
insert400 = []


merge400 = mergetimelist+ blank*14
heap400 = heaptimelist+ blank*14
insert400 = inserttimelist+ blank*14

mergetimelist=[]
heaptimelist=[]
inserttimelist=[]

print("-----------Merging Each  " + str(noOfFiles/8) +  " files (iteration-3)-----------")
#noOfFilesIteration1 = noOfFiles/2
#-------Merging iteration-2
for i in range(1,16,16):
	x = i+1
	y = x+1
	j = y+1
	q = j+1
	w = q+1
	e = w+1
	r = e+1
	p1 = str(i) + str(x) + str(y) + str(j) + str(q) + str(w) + str(e) + str(r)
	file1 = "Iteration2/data" + str(p1) + ".txt"		
	i = r+1
	x = i+1
	y = x+1
	j = y+1
	q = j+1
	w = q+1
	e = w+1
	r = e+1
	p2 = str(i) + str(x) + str(y) + str(j) + str(q) + str(w) + str(e) + str(r)
	file2 = "Iteration2/data" +  str(p2)+ ".txt"
	list1 = read_integers(file1)
	list2 = read_integers(file2)
	mergeList3 = mergeList2 = mergeList1  = list1 + list2

	start_time_merge = time.time()
	mergeSort(mergeList1)
	timemerge = (time.time() - start_time_merge)
	totalTimeMerge = totalTimeMerge + timemerge
	print("merge sort :")
	#print(list1)
	print("--- %s seconds ---" % timemerge)
	mergetimelist.append(timemerge)

	start_time_insertion = time.time()
	insertionSort(mergeList2)
	timeinsert = (time.time() - start_time_merge)
	totalTimeInsertion = totalTimeInsertion + timeinsert
	print("insertion sort :")
	#print(list2)
	print("--- %s seconds ---" % timeinsert)
	inserttimelist.append(timeinsert)


	start_time_heap = time.time()
	heapSort(mergeList3)
	timeheap = (time.time() - start_time_heap)
	totalTimeheap = totalTimeheap + timeheap	
	print("heap sort :")
	#print(list1)
	print("--- %s seconds ---" % timeheap)
	heaptimelist.append(timeheap)

	mergeFileName ="Iteration3Final/data" + str(p1) + str(p2) + ".txt" 
	print("-----------Creating file  " + str(mergeFileName) +  "-----------")
	mergeFile = open( mergeFileName, 'w')
	for x in mergeList1:
		mergeFile.write(str(x)+"\n")
print("-----------Successfully Merge Each  " + str(noOfFiles/8) +  " files into " + str(noOfFiles/16) +"(iteration-3)-----------")
print("-----------Total time taken by merge sort " + str(totalTimeMerge) +"  -----------")
print("-----------Total time taken by insertion sort " + str(totalTimeInsertion) +"  -----------")
print("-----------Total time taken by heap sort " + str(totalTimeheap) +"  -----------")

merge800 = []
heap800 = []
insert800 = []

merge800 = mergetimelist + blank*15
heap800 = heaptimelist + blank*15
insert800 = inserttimelist + blank*15

dfMerge = pd.DataFrame.from_dict({'50K':merge50,'100K':merge100,'200K':merge200,'400K':merge400,'800K':merge800,})
dfMerge.to_excel('merge.xlsx', header=True, index=False)

dfInsertion = pd.DataFrame.from_dict({'50K':insert50,'100K':insert100,'200K':insert200,'400K':insert400,'800K':insert800,})
dfInsertion.to_excel('insert.xlsx', header=True, index=False)

dfheap = pd.DataFrame.from_dict({'50K':heap50,'100K':heap100,'200K':heap200,'400K':heap400,'800K':heap800,})
dfheap.to_excel('heap.xlsx', header=True, index=False)


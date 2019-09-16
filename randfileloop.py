DataFile = open( 'Data.txt', 'r')
lines = DataFile.readlines()

for i in range(1,7):
	file_name="data" + str(i) + ".txt"
	print(file_name)
	startReading = 0 
	endReading = 100
	increaseRate = 50
	print(lines[startReading:endReading])
	startReading = startReading + endReading + 1
	endReading = endReading + increaseRate




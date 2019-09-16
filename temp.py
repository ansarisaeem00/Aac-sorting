from tabulate import tabulate
name = ["saeem", "Ash",""]
age = ["20","22","18","29"]

first = ["1","3","1","5","6","7","9","3","6","7","0","1","5","6","8","4"]
second =["2","3","1","5","6","7","9","2","","","","","","","","",""]
third =["3","3","0","5","","","","","","","","","","","","",""]
fourth =["4","3","","","","","","","","","","","","","","",""]
#print(tabulate([first, second,third,fourth],headers=['50K', '100K' ,"200K","400K","800K"]))
#DataFileWrite = open( "Analyse.txt", 'w')
for i in first:
	print(tabulate([first[int(i)]]))

#DataFileWrite.write(tabulate([first, second,third,fourth],headers=['50K', '100K' ,"200K","400K","800K"])) 
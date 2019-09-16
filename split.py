DataFile = open ('Data.txt')
lines=DataFile.readlines()
f1 = open('Data1.txt' , 'w')

f1.write(repr(lines[0:100]) + '\n')

f1.close()
DataFile.close()


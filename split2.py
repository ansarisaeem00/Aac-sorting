f = open( 'Data.txt', 'r' )
f1 = open('Data1.txt','w')
lines = f.readlines()

for x in lines[0:50]:
	f1.write(x)

	
f.close()
f1.close()	

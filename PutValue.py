value = 10
f = open( 'value1.txt', 'w' )
f.write( repr(value) + '\n' )
f.close()

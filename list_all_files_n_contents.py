import os

objFile = open( 'new_file.py', 'w' )

for file_name in os.listdir('./') :
	if file_name.endswith( '.py' ) :
		objFile.write( '#'*10 )
		objFile.write( file_name )
		objFile.write( '#'*10 )
		with open( file_name, 'r' ) as file_to_read :
			line = file_to_read.readline()
			while line :
				objFile.write( line )
				line = file_to_read.readline()


objFile.close()
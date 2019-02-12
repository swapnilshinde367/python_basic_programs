import json
from datetime import datetime
import matplotlib.pyplot as plt

months = {}

with open( 'json_file.json' ) as json_file :
	line = json_file.read()
	line = json.loads( line )
	for i in line :
		jsondate = line[i].split('/')
		datem = datetime( int(jsondate[2]), int(jsondate[0]), int(jsondate[1]) ).strftime('%b')
		if( datem not in months ) :
			months[datem] = 1
		else :
			months[datem] = months[datem] + 1

plt.bar( months.keys(), months.values() )
plt.show()
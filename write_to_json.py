import json

birthdays = {
		'Albert Einstein': '03/14/1879',
		'Benjamin Franklin': '01/17/1706',
		'Ada Lovelace': '12/10/1815',
		'Donald Trump': '06/14/1946',
		'Rowan Atkinson': '01/6/1955'}

with open( 'json_file.json', 'a' ) as json_file :
	json_file.writelines( json.dumps( birthdays ) )
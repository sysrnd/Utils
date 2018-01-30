#mkf_utils
#arturoalcibia@hotmail.com
#finds an specific path from environment vars
import os
def findEnv_(envWord, keyWordSection, keywordOne, keywordTwo):
	path = ''
	try:
		envVar =os.environ[envWord]
	except KeyError:
		return None
	envVar = envVar.split(';')

	for x in envVar:
		if x.find(keyWordSection) != -1:
			if x.find(keywordOne) != -1 or x.find(keywordTwo):
				path =  x

	return path


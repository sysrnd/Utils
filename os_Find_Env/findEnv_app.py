#mkf_utils
#arturoalcibia@hotmail.com
#finds an specific path from environment vars
import os
def findEnvVar_(envWord = 'MAYA_SCRIPT_PATH', keyWordSection = 'Scripts', keywordOne = 'MKF', keywordTwo = 'RnD'):
	
	path = ''
	try:
		envVar = os.environ[envWord]
	except KeyError:
		return None
	envVar = envVar.split(';')

	for x in envVar:
		print x
		#if x.find(keyWordSection) != -1:
		if x.find(keywordOne) != -1 or x.find(keywordTwo) != -1:
			path =  x

	return path
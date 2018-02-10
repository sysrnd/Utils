#mkf_utils
#arturoalcibia@hotmail.com
#finds an specific path from environment vars
import maya.mel as mel
def findEnvVar_(envWord = 'MAYA_SCRIPT_PATH', keyWordSection = 'Scripts', keywordOne = 'MKF', keywordTwo = 'RnD'):
	
	path = ''
	envVar = mel.eval('getenv "MAYA_SCRIPT_PATH";')
	envVar = envVar.split(';')

	for x in envVar:
		if x.find(keywordOne) != -1 or x.find(keywordTwo) != -1:
		    if x.find('Shelves') == -1:
		    	print x
			    path =  x

	return path

print findEnvVar_()
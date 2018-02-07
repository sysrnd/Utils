#create dirs in case they dont exist
import os
import datetime
import getpass
import maya.cmds as cmds

class CreateLog(object):
	def __init__(self):

		self.date = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
		self.user = getpass.getuser()
		self.traceFile = os.environ[ "MAYA_CMD_FILE_OUTPUT"]

	def mainLog(self, app):

		path = self.checkDir(app)
		logName = self.genName()
		self.createLog(path, logName)
	def createLog(self, path, logName):
		traceFile = path + logName
		descriptor = cmds.cmdFileOutput(o=traceFile)
		return descriptor

	def closeLog(self):
		if descriptor != -1:
			cmds.cmdFileOutput( close=descriptor )


	def checkDir(self, app):
		appPath = self.traceFile + app
		if not os.path.exists(appPath):
			os.mkdir(appPath)

		return appPath

	def genName(self):

		logName = self.date + '_' + self.user
		return logName

log = CreateLog()
log.mainLog('CreateAlembics')
log.closeLog()
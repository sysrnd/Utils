import maya.cmds as cmds

def shapeToDummy(ctrl):
	#cmds.select(cl=True)
	tempGrp = cmds.group(em=True, n=ctrl + '_tempGRP')

	shapes = cmds.listRelatives(ctrl, s=True)
	for shape in shapes:
		cmds.parent(shape, tempGrp, r=True, s=True)
	return tempGrp

def shapeToCtrl(ctrl, grp):
	shapes = cmds.listRelatives(grp, s=True)

	for shape in shapes:
		newShape = cmds.parent(shape, ctrl, s=True, r=False)[0]
		parentShape = cmds.listRelatives(newShape, p=True)[0]
		cmds.makeIdentity(parentShape, apply=True, t=1, r=1, s=0, n=0)
		newShape = cmds.parent(newShape, ctrl, s=True, r=True)
		cmds.delete(parentShape)
	cmds.delete(grp)
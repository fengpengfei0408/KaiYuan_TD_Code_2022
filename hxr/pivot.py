import maya.cmds as cmds

class Pivots():

    def __init__(self):
        self.selected = None

    def PivotMakeZero(self):
        self.selected = cmds.ls(sl=True)
        for i in self.selected:
            cmds.xform(i, cp=True)
            cmds.makeIdentity(i, a=True)
            #cmds.move(0, 0, 0, i + '.rotatePivot', i + '.scalePivot', ws=True)
            cmds.move(0, 0, 0, i, ws=True)
            #cmds.delete(self.selected, ch=True)


p=Pivots()
p.PivotMakeZero()


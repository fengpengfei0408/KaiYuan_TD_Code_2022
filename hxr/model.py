import maya.cmds as cmds

class Model():

    def __init__(self):
        self.selected = None

    def ModelMakeZero(self):
        self.selected = cmds.ls(sl=True)
        for i in self.selected:
            cmds.xform(i, cp=True)
            cmds.makeIdentity(i, a=True)
            lcation = cmds.xform(i, q=1, ws=True, rp=1)
            cmds.xform(i,t=[-lcation[0], -lcation[1], -lcation[2]])
            #cmds.move(0 ,0 ,0, i, ws=True)

            cmds.delete(self.selected, ch=True)

            
            
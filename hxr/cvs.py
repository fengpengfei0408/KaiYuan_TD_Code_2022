# coding=utf8
import maya.cmds as mc

class CVs():
    def __init__(self):
        self.obj = None

    def DeleteHistory(self):
        topDagList = mc.ls(assemblies=True)
        mc.select(topDagList)
        mc.delete(ch=True)
        mc.select(cl=True)


    def MakeZero(self):
        self.obj = mc.ls(sl=True)
        self.DeleteHistory()
        mc.select(self.obj)
        mc.lattice(oc=True)
        self.DeleteHistory()
        mc.select(self.obj)

#c = CVs()
#c.MakeZero()



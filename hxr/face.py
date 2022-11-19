# coding=utf8
import maya.cmds as mc

class Face():

    def Check(self):
        faceList = []
        infoEdgeList = []
        npList = []

        faceList = mc.ls(sl=True, fl=True)
        infoEdge = mc.polyInfo(fe=True)
        for i in infoEdge:
            a = i.split()
            nList = []
            for n in a:
                if n.isdigit():
                    nList.append(n)
            npList.append(nList)

        mc.select(clear=True)
        for i in npList:
            if len(i) > 4:
                n = npList.index(i)
                mc.select(faceList[n], add=True)

# coding=utf8
import maya.cmds as mc

class Hole():
    def CheckHole(self):
        edgeList = mc.ls(sl=True, fl=True)
        edgeInfo = mc.polyInfo(ef=True)
        npList = []
        fList = []
        fsList = []
        fDict = {}
        b = -1

        for i in edgeInfo:
            a = i.split()
            nList = []
            for n in a:
                if n.isdigit():
                    nList.append(n)
            npList.append(nList)
        mc.select(cl=True)
        for i in npList:
            b += 1
            fDict[b] = i

        for i in npList:
            if len(i) == 1:
                fList.append(i)
        if fList != []:
            mc.confirmDialog(m='There are holes', button='ok')
        else:
            mc.confirmDialog(m='There are no holes', button='ok')

        for i in fList:
            if not i in fsList:
                fsList.append(i)

        for i in fsList:
            n = list(k for k, v in fDict.items() if v == i)
            for a in n:
                mc.select(edgeList[int(a)], add=True)
        mc.polyCloseBorder(mc.ls(sl=True))






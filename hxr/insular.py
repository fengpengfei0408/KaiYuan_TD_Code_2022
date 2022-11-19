# coding=utf8
import maya.cmds as mc
class Insular():

    def InsularVertex(self):
        vertexList = mc.ls(sl=True, fl=True)
        infoList = mc.polyInfo(ve=True)
        edgeList = []
        iList = []
        ieList = []
        edgeDict = {}
        b = -1
        for i in infoList:
            aList = []
            for a in i.split():
                if a.isdigit():
                    aList.append(a)
            edgeList.append(aList)

        mc.select(cl=True)
        for i in edgeList:
            b += 1
            edgeDict[b] = i

        for i in edgeList:
            if len(i) < 2:  ########
                iList.append(i)

        if iList == []:
            mc.confirmDialog(m='There are no insular vertex.', button='ok')
        else:
            mc.confirmDialog(m='There are insular vertex!', button='ok')

        for i in iList:
            if not i in ieList:
                ieList.append(i)

        for i in ieList:
            n = list(k for k, v in edgeDict.items() if v == i)
            for a in n:
                mc.select(vertexList[int(a)], add=True)




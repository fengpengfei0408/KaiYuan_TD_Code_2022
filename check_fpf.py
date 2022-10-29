# coding=utf-8
import maya.OpenMaya as om
import pymel.core as pm
import maya.cmds as mc
from PySide2 import QtWidgets, QtCore, QtGui
class GEO_CHECK_UI(QtWidgets.QWidget):
    def __init__(self):
        super(GEO_CHECK_UI, self).__init__()
        self.setWindowTitle("CHECK WINDOW")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.buildUI()

    def buildUI(self):
        layout = QtWidgets.QGridLayout(self)
        self.item_1 = QtWidgets.QCheckBox("Check for overlap")
        self.item_1.toggled.connect(self.method_1)

        self.button_1 = QtWidgets.QPushButton('check')
        self.button_1.clicked.connect(self.check)

        self.button_2 = QtWidgets.QPushButton('select')
        self.button_2.clicked.connect(self.select)

        self.button_3 = QtWidgets.QPushButton('fix')
        self.button_3.clicked.connect(self.fix)

        layout.addWidget(self.item_1, 0, 0)
        layout.addWidget(self.button_1, 0, 2)
        layout.addWidget(self.button_2, 0, 3)
        layout.addWidget(self.button_3, 0, 4)

    def method_1(self):
        pass

    def check(self):
        global node
        self.dict = {}
        self.translate = []
        self.morevtx = []
        self.name = []
        self.rename = []
        self.check_List = []
        nodeList = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(nodeList)
        dagPath = om.MDagPath()
        node_iter = om.MItSelectionList(nodeList)
        while not node_iter.isDone():
            node_iter.getDagPath(dagPath)
            node = dagPath.partialPathName()
            iterator = om.MItMeshVertex(pm.PyNode(node).__apiobject__())
            while not iterator.isDone():
                point = iterator.position()
                tuple = (point.x,point.y,point.z)
                index = iterator.index()
                item = node+'.vtx[{0}]'.format(index)
                self.name.append(item)#所有点名字列表
                self.translate.append(tuple)#所有点位置列表
                self.dict[item] = tuple
                edge_IntArray = om.MIntArray()
                iterator.getConnectedEdges(edge_IntArray)
                print(edge_IntArray)
                if len(edge_IntArray) < 3:
                    self.check_List.append(item)
                iterator.next()
            print (self.check_List)
            for i in self.translate:
                a = self.translate.count(i)
                for item in self.dict.items():
                    if a >= 2:
                        if item[1] == i:
                            if item[0] in self.check_List:
                                self.morevtx.append(i)#重合点位置列表
                                if item in self.rename:
                                    pass
                                else:
                                    self.rename.append(item[0])#重合点名称列表
            if len(self.morevtx)>0:
                print(node+' have coincident point')
            else:
                print(node+' not have coincident point')
            node_iter.next()
    def select(self):
        mc.select(clear = True)
        for item in self.rename:
            mc.select(item,add = True)
    def fix(self):
        mc.Delete(mc.ls(sl=True))
        print('Deleting completed')

def showUI():
    ui = GEO_CHECK_UI()
    ui.show()
    return ui


ui = showUI()

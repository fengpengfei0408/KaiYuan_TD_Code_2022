from maya import cmds
import pymel.core as pm
from PySide2 import QtGui,QtCore,QtWidgets
import maya.OpenMaya as OpenMaya


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.buildUI()

    def buildUI(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        mayacheck = MayaCheck()
        self.layout.addWidget(mayacheck)

class MayaCheck(QtWidgets.QWidget):
    def __init__(self):
        super(MayaCheck, self).__init__()
        self.buildUI()

    def buildUI(self):
        self.layout = QtWidgets.QGridLayout()

        #设置标题
        title = QtWidgets.QLabel()
        title.setText("MAYA CHECK")

        self.coincidentPoint()

        self.isolatedPoint()

        self.illegalSurface()

        self.setLayout(self.layout)
        self.layout.addWidget(title,0,0)

    def warningMessage(self):
        warn = QtWidgets.QMessageBox.warning(self,"warning","You did not select the object, please select")

    #检查并删除重合点(未完成)
    def coincidentPoint(self):

        #检查重合点
        func = QtWidgets.QCheckBox('check coincident point')
        self.layout.addWidget(func, 1, 0)

        # 检查重合点按钮
        btn1 = QtWidgets.QPushButton("check")
        btn1.clicked.connect(self.check1)
        self.layout.addWidget(btn1, 1, 1)

        # 选择要删除的重合点
        btn2 = QtWidgets.QPushButton("select")
        btn2.clicked.connect(self.select1)
        self.layout.addWidget(btn2, 1, 2)

        # 删除重合点
        btn3 = QtWidgets.QPushButton("fix")
        btn3.clicked.connect(self.fixVertex)
        self.layout.addWidget(btn3, 1, 3)

        #列表存放重合点
        self.concident = []

    def check1(self):

        #定义一个MSelection并将所选择物体添加至MSelection
        sel_lst = OpenMaya.MSelectionList()

        OpenMaya.MGlobal.getActiveSelectionList(sel_lst)

        #判断是否选择物体，如果没有则提示用户选择
        if sel_lst.length() == 0:
            self.warningMessage()

        dag_path = OpenMaya.MDagPath()

        lst_iter = OpenMaya.MItSelectionList(sel_lst)

        #定义一个字典存放点的名称和坐标
        self.points = {}

        # 存放重复点
        concident = []

        while not lst_iter.isDone():
            lst_iter.getDagPath(dag_path)

            iterators = OpenMaya.MItMeshVertex(dag_path)

            while not iterators.isDone():
                #通过dagpath获取物体名称并通过点的索引找到点的名字
                self.pname = dag_path.partialPathName() + '.vtx[{0}]'.format(iterators.index())

                point = iterators.position()
                self.points[self.pname] = point.x,point.y,point.z

                iterators.next()

            lst_iter.next()


        # 点坐标列表
        vallist = self.points.values()

        # 循环每一个字典并在循环刚开始时移除vallist列表中的第一个值
        for item in self.points.items():
            vallist.pop(0)

            for val in vallist:
                # 比较点坐标值，相同坐标的点添加至re列表
                if item[1] == val:

                    concident.append(item[0])

            #将列表内重复的点删除
            self.concident = list(set(concident))
        print self.concident

        #如果没有重合点弹出信息框
        if len(self.concident) == 0 and sel_lst.length() != 0 :
            QtWidgets.QMessageBox.information(self,"Information","There is no concident vertex")

    def select1(self):
        #选择重复点
        pm.select(clear = True)

        #当没有检查模型或没有重合点时发出警告
        if len(self.concident) == 0:
            QtWidgets.QMessageBox.warning(self,"warning","You haven't checked it yet or no concident vertex")

        #循环重合点并选择
        for p in self.concident:
            pm.select(p,add = True)


    #检查并删除孤立点
    def isolatedPoint(self):
        #检查孤立顶点
        func = QtWidgets.QCheckBox('check isolatedpoint point')
        self.layout.addWidget(func,2,0)

        # 检查孤立点按钮
        btn1 = QtWidgets.QPushButton("check")
        btn1.clicked.connect(self.check2)
        self.layout.addWidget(btn1, 2, 1)

        # 选择要删除的孤立点
        btn2 = QtWidgets.QPushButton("select")
        btn2.clicked.connect(self.select2)
        self.layout.addWidget(btn2, 2, 2)

        # 删除孤立点
        btn3 = QtWidgets.QPushButton("fix")
        btn3.clicked.connect(self.fixVertex)
        self.layout.addWidget(btn3, 2, 3)

        # 定义一个列表存放点的名称
        self.isolatedpoint = []

    def check2(self):
        # 定义一个MSelection并将所选择物体添加至MSelection
        sel_lst = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(sel_lst)

        # 判断是否选择物体，如果没有则提示用户选择
        if sel_lst.length() == 0:
            self.warningMessage()

        dag_path = OpenMaya.MDagPath()

        lst_iter = OpenMaya.MItSelectionList(sel_lst)

        while not lst_iter.isDone():
            lst_iter.getDagPath(dag_path)

            iterators = OpenMaya.MItMeshVertex(dag_path)

            #整数类型数组存放点相关边
            arrey = OpenMaya.MIntArray()

            while not iterators.isDone():
                #通过dagpath获取物体名称并通过点的索引找到点的名字
                pname = dag_path.partialPathName() + '.vtx[{0}]'.format(iterators.index())

                iterators.getConnectedEdges(arrey)

                if arrey.length() < 3 :
                    self.isolatedpoint.append(pname)

                iterators.next()

            lst_iter.next()

        print self.isolatedpoint

        #如果没有孤立点，弹出信息
        if len(self.isolatedpoint) == 0 and sel_lst.length() != 0:
            QtWidgets.QMessageBox.information(self, "Information", "There is no isolated vertex ")

    def select2(self):
        #选择孤立点
        pm.select(clear = True)

        #当没检查模型或没有孤立点时发出警告
        if len(self.isolatedpoint) == 0:
            QtWidgets.QMessageBox.warning(self,"warning","You haven't checked it yet or no isolated vertex ")

        #循环孤立点列表将其进行选择
        for p in self.isolatedpoint:
            pm.select(p,add = True)

    def fixVertex(self):
        #删除所选中的点
        pm.delete()


    #检查多边面
    def illegalSurface(self):
        #检查多边面
        func = QtWidgets.QCheckBox('check illegal surface')
        self.layout.addWidget(func, 3, 0)

        #检查多边面按钮
        btn1 = QtWidgets.QPushButton("check")
        btn1.clicked.connect(self.check3)
        self.layout.addWidget(btn1, 3, 1)

        #修复按钮
        btn2 = QtWidgets.QPushButton("fix")
        btn2.clicked.connect(self.fixSurface)
        self.layout.addWidget(btn2, 3, 2)

        #列表存放多边面
        self.isurface = []
    def check3(self):
        # 定义一个MSelection并将所选择物体添加至MSelection
        sel_lst = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(sel_lst)

        # 判断是否选择物体，如果没有则提示用户选择
        if sel_lst.length() == 0:
            self.warningMessage()

        dag_path = OpenMaya.MDagPath()

        lst_iter = OpenMaya.MItSelectionList(sel_lst)

        while not lst_iter.isDone():
            lst_iter.getDagPath(dag_path)

            iterators = OpenMaya.MItMeshPolygon(dag_path)

            # 整数类型数组传入面上的边
            arrey = OpenMaya.MIntArray()
            while not iterators.isDone():
                fname = dag_path.partialPathName() + '.f[{0}]'.format(iterators.index())

                iterators.getEdges(arrey)

                if arrey.length() >4 :
                    self.isurface.append(fname)

                iterators.next()

            lst_iter.next()

        #如果没有多边面，弹出提示框
        if len(self.isurface) == 0 and sel_lst.length() != 0:
            QtWidgets.QMessageBox.information(self, "Information", "There is no illegal surface ")

    def fixSurface(self):
        pm.select(clear=True)

        #当没有检查模型或没有多变面时发出警告
        if len(self.isurface) == 0:
            QtWidgets.QMessageBox.warning(self, "warning", "You haven't checked it yet or no illegal surface ")

        #循环多边面并选择
        for f in self.isurface:
            pm.select(f, add=True)

def showUI():
    '''
    展示并返回UI
    Returns:
        QDiolog
    '''
    ui = mainWindow()
    ui.show()
    return ui

UI =showUI()







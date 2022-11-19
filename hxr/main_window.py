#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as mc
import face
import cvs
import pivot
import model
import hole
import insular

def MayaMainWindow():
    mainWindowPtr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(mainWindowPtr), QWidget)

class MyWindow(QDialog,QFont,face.Face,cvs.CVs,pivot.Pivots,model.Model,hole.Hole,insular.Insular):

    def __init__(self, parent=MayaMainWindow()):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("check face")
        self.resize(400,500)
        self.BuildUI()


    def BuildUI(self):
        self.f=face.Face()
        self.c=cvs.CVs()
        self.p=pivot.Pivots()
        self.m=model.Model()
        self.h=hole.Hole()
        self.i=insular.Insular()

        self.label1=QLabel('Check face',self)
        #self.label.setStyleSheet("font:20px'SimSun'")
        self.label1.setFont(QFont("SimSun", 10))
        self.label1.move(30,35)

        self.label2=QLabel('CVs goes to zero',self)
        self.label2.setFont(QFont("SimSun", 10))
        self.label2.move(30, 85)

        self.label3=QLabel('Model goes to zero',self)
        self.label3.setFont(QFont("SimSun", 10))
        self.label3.move(30, 135)

        self.label4=QLabel('Pivot goes to zero',self)
        self.label4.setFont(QFont("SimSun", 10))
        self.label4.move(30, 185)

        self.label5=QLabel('Holes filling',self)
        self.label5.setFont(QFont("SimSun", 10))
        self.label5.move(30, 235)

        self.label6=QLabel('Look for insular vertex',self)
        self.label6.setFont(QFont("SimSun", 10))
        self.label6.move(30, 285)

        self.btn1 = QPushButton('check',self)
        #self.btn.setStyleSheet("font:20px'SimHei'")
        self.btn1.setFont(QFont("SimHei", 9))
        self.btn1.setFixedSize(70,30)
        self.btn1.move(260,30)
        self.btn1.clicked.connect(self.f.Check)

        self.btn2 = QPushButton('cvs zero',self)
        self.btn2.setFont(QFont("SimHei", 9))
        self.btn2.setFixedSize(80,30)
        self.btn2.move(260,80)
        self.btn2.clicked.connect(self.c.MakeZero)

        self.btn3 = QPushButton('model zero',self)
        self.btn3.setFont(QFont("SimHei", 9))
        self.btn3.setFixedSize(100,30)
        self.btn3.move(260,130)
        self.btn3.clicked.connect(self.m.ModelMakeZero)

        self.btn4 = QPushButton('pivot zero',self)
        self.btn4.setFont(QFont("SimHei", 9))
        self.btn4.setFixedSize(100,30)
        self.btn4.move(260,180)
        self.btn4.clicked.connect(self.p.PivotMakeZero)

        self.btn5 = QPushButton('fill hole',self)
        self.btn5.setFont(QFont("SimHei", 9))
        self.btn5.setFixedSize(100,30)
        self.btn5.move(260,230)
        self.btn5.clicked.connect(self.h.CheckHole)

        self.btn6 = QPushButton('insular',self)
        self.btn6.setFont(QFont("SimHei", 9))
        self.btn6.setFixedSize(70,30)
        self.btn6.move(260,280)
        self.btn6.clicked.connect(self.i.InsularVertex)

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



if __name__ == "__main__":
    try:
        myWindow.close() #pylint:disable=E0601
        myWindow.deleteLater()
    except:
        pass

    myWindow = MyWindow()
    myWindow.show()








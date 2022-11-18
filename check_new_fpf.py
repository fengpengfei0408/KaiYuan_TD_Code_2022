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
        self.item_1.setChecked(True)
        self.item_1.stateChanged.connect(self.method_overlap)

        self.button_overlap_1 = QtWidgets.QPushButton('check')
        self.button_overlap_1.clicked.connect(self.check_overlap)

        self.button_overlap_2 = QtWidgets.QPushButton('select')
        self.button_overlap_2.clicked.connect(self.select_overlap)

        self.button_overlap_3 = QtWidgets.QPushButton('fix')
        self.button_overlap_3.clicked.connect(self.fix_overlap)

        self.item_2 = QtWidgets.QCheckBox("Check for cv")
        self.item_2.setChecked(True)
        self.item_2.stateChanged.connect(self.method_cv)

        self.button_cv_1 = QtWidgets.QPushButton('check')
        self.button_cv_1.clicked.connect(self.check_cv)

        self.button_cv_2 = QtWidgets.QPushButton('select')
        self.button_cv_2.clicked.connect(self.select_cv)

        self.button_cv_3 = QtWidgets.QPushButton('fix')
        self.button_cv_3.clicked.connect(self.fix_cv)

        self.item_3 = QtWidgets.QCheckBox("Check illegal face")
        self.item_3.setChecked(True)
        self.item_3.stateChanged.connect(self.method_illegal_face)

        self.button_illegal_1 = QtWidgets.QPushButton('check')
        self.button_illegal_1.clicked.connect(self.check_illegal)

        self.button_illegal_2 = QtWidgets.QPushButton('select')
        self.button_illegal_2.clicked.connect(self.select_illegal)

        self.button_illegal_3 = QtWidgets.QPushButton('fix')
        self.button_illegal_3.setDisabled(True)

        self.item_4 = QtWidgets.QCheckBox("Check for model pivot")
        self.item_4.setChecked(True)
        self.item_4.stateChanged.connect(self.method_pivot)

        self.button_pivot_1 = QtWidgets.QPushButton('check')
        self.button_pivot_1.clicked.connect(self.check_pivot)

        self.button_pivot_2 = QtWidgets.QPushButton('fix')
        self.button_pivot_2.clicked.connect(self.fix_pivot)

        self.item_5 = QtWidgets.QCheckBox("Check for model return to the origin")
        self.item_5.setChecked(True)
        self.item_5.stateChanged.connect(self.method_model_zero)

        self.button_mz_1 = QtWidgets.QPushButton('check')
        self.button_mz_1.clicked.connect(self.check_model_zero)

        self.button_mz_2 = QtWidgets.QPushButton('fix')
        self.button_mz_2.clicked.connect(self.fix_model_zero)

        self.item_6 = QtWidgets.QCheckBox("Check overlapping surface")
        self.item_6.setChecked(True)
        self.item_6.stateChanged.connect(self.method_overlap_face)

        self.button_of_1 = QtWidgets.QPushButton('check')
        self.button_of_1.clicked.connect(self.check_overlap_face)

        self.button_of_2 = QtWidgets.QPushButton('select')
        self.button_of_2.clicked.connect(self.select_overlap_face)

        self.button_of_3 = QtWidgets.QPushButton('fix')
        self.button_of_3.clicked.connect(self.fix_overlap_face)
        self.button_of_3.setDisabled(True)

        self.item_7 = QtWidgets.QCheckBox("Check the model normals")
        self.item_7.setChecked(True)
        self.item_7.stateChanged.connect(self.method_model_normal)

        self.button_mn_1 = QtWidgets.QPushButton('check')
        self.button_mn_1.clicked.connect(self.check_model_normal)

        self.button_mn_2 = QtWidgets.QPushButton('select')
        self.button_mn_2.clicked.connect(self.select_model_normal)

        self.button_mn_3 = QtWidgets.QPushButton('fix')
        self.button_mn_3.clicked.connect(self.fix_model_normal)

        self.item_8 = QtWidgets.QCheckBox("Check the model for holes")
        self.item_8.setChecked(True)
        self.item_8.stateChanged.connect(self.method_model_hole)

        self.button_mh_1 = QtWidgets.QPushButton('check')
        self.button_mh_1.clicked.connect(self.check_model_hole)

        self.button_mh_2 = QtWidgets.QPushButton('select')
        self.button_mh_2.clicked.connect(self.select_model_hole)

        self.button_mh_3 = QtWidgets.QPushButton('fix')
        self.button_mh_3.clicked.connect(self.fix_model_hole)

        self.item_9 = QtWidgets.QCheckBox("Check the model for isolated vertex")
        self.item_9.setChecked(True)
        self.item_9.stateChanged.connect(self.method_isolated_vertex)

        self.button_iv_1 = QtWidgets.QPushButton('check')
        self.button_iv_1.clicked.connect(self.check_isolated_vertex)

        self.button_iv_2 = QtWidgets.QPushButton('select')
        self.button_iv_2.clicked.connect(self.select_isolated_vertex)

        self.button_iv_3 = QtWidgets.QPushButton('fix')
        self.button_iv_3.clicked.connect(self.fix_isolated_vertex)

        self.item_10 = QtWidgets.QCheckBox("freeze transformations and delete history")
        self.item_10.setChecked(True)
        self.item_10.stateChanged.connect(self.method_freeze_delete)

        self.button_fd_1 = QtWidgets.QPushButton('freeze')
        self.button_fd_1.clicked.connect(self.freeze_transformations)

        self.button_fd_2 = QtWidgets.QPushButton('delete')
        self.button_fd_2.clicked.connect(self.delete_history)


        layout.addWidget(self.item_1, 0, 0)
        layout.addWidget(self.button_overlap_1, 0, 2)
        layout.addWidget(self.button_overlap_2, 0, 3)
        layout.addWidget(self.button_overlap_3, 0, 4)

        layout.addWidget(self.item_2, 1, 0)
        layout.addWidget(self.button_cv_1, 1, 2)
        layout.addWidget(self.button_cv_2, 1, 3)
        layout.addWidget(self.button_cv_3, 1, 4)

        layout.addWidget(self.item_3, 2, 0)
        layout.addWidget(self.button_illegal_1, 2, 2)
        layout.addWidget(self.button_illegal_2, 2, 3)
        layout.addWidget(self.button_illegal_3, 2, 4)

        layout.addWidget(self.item_4, 3, 0)
        layout.addWidget(self.button_pivot_1, 3, 2)
        layout.addWidget(self.button_pivot_2, 3, 3, 1, 2)

        layout.addWidget(self.item_5, 4, 0)
        layout.addWidget(self.button_mz_1, 4, 2)
        layout.addWidget(self.button_mz_2, 4, 3, 1, 2)

        layout.addWidget(self.item_6, 5, 0)
        layout.addWidget(self.button_of_1, 5, 2)
        layout.addWidget(self.button_of_2, 5, 3)
        layout.addWidget(self.button_of_3, 5, 4)

        layout.addWidget(self.item_7, 6, 0)
        layout.addWidget(self.button_mn_1, 6, 2)
        layout.addWidget(self.button_mn_2, 6, 3)
        layout.addWidget(self.button_mn_3, 6, 4)

        layout.addWidget(self.item_8, 7, 0)
        layout.addWidget(self.button_mh_1, 7, 2)
        layout.addWidget(self.button_mh_2, 7, 3)
        layout.addWidget(self.button_mh_3, 7, 4)

        layout.addWidget(self.item_9, 8, 0)
        layout.addWidget(self.button_iv_1, 8, 2)
        layout.addWidget(self.button_iv_2, 8, 3)
        layout.addWidget(self.button_iv_3, 8, 4)

        layout.addWidget(self.item_10, 9, 0, 1, 2)
        layout.addWidget(self.button_fd_1, 9, 3)
        layout.addWidget(self.button_fd_2, 9, 4)

    # 检查重合点

    def method_overlap(self):
        if self.item_1.isChecked() == True:
            self.button_overlap_1.setDisabled(False)
            self.button_overlap_2.setDisabled(False)
            self.button_overlap_3.setDisabled(False)
        else:
            self.button_overlap_1.setDisabled(True)
            self.button_overlap_2.setDisabled(True)
            self.button_overlap_3.setDisabled(True)

    def check_overlap(self):
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
        if nodeList.length() == 0:
            print('Please select object!')
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
    def select_overlap(self):
        mc.select(clear = True)
        for item in self.rename:
            mc.select(item,add = True)
    def fix_overlap(self):
        mc.Delete(mc.ls(sl=True))
        print('Deleting completed')




#模型CV值归零

    def method_cv(self):
        if self.item_2.isChecked() == True:
            self.button_cv_1.setDisabled(False)
            self.button_cv_2.setDisabled(False)
            self.button_cv_3.setDisabled(False)
        else:
            self.button_cv_1.setDisabled(True)
            self.button_cv_2.setDisabled(True)
            self.button_cv_3.setDisabled(True)

    def check_cv(self):
        self.cv_list = []
        self.select_List = mc.ls(sl=True)
        for select_object in self.select_List:
            mIt_object = om.MItMeshVertex(pm.PyNode(select_object).__apiobject__())
            while not mIt_object.isDone():
                index = mIt_object.index()
                mIt_name = mc.listRelatives(select_object, ad=True)[0] + ".pnts[{0}]".format(index)
                object_pntx = mIt_name + ".pntx"
                object_pnty = mIt_name + ".pnty"
                object_pntz = mIt_name + ".pntz"
                object_pntx_value = mc.getAttr(object_pntx)
                object_pnty_value = mc.getAttr(object_pnty)
                object_pntz_value = mc.getAttr(object_pntz)
                if object_pntx_value != 0:
                    self.cv_list.append(mIt_name)
                elif object_pnty_value != 0:
                    if mIt_name in self.cv_list:
                        pass
                    else:
                        self.cv_list.append(mIt_name)
                elif object_pntz_value != 0:
                    if mIt_name in self.cv_list:
                        pass
                    else:
                        self.cv_list.append(mIt_name)
                mIt_object.next()
        if len(self.cv_list) == 0:
            print ("cv value of the model has been reduced to zero!")
        else:
            print ("The point at which the cv value does not return to zero:{0}".format(self.cv_list))

    def select_cv(self):
        for point in self.cv_list:
            mc.select(point, add=True)

    def fix_cv(self):
        ffd_la = mc.lattice(oc = True)
        for select_object in self.select_List:
            mc.delete(select_object,constructionHistory=True)
        print("cv value has been reduced to zero!")





# 检查多边面

    def method_illegal_face(self):
        if self.item_3.isChecked() == True:
            self.button_illegal_1.setDisabled(False)
            self.button_illegal_2.setDisabled(False)
        else:
            self.button_illegal_1.setDisabled(True)
            self.button_illegal_2.setDisabled(True)

    def check_illegal(self):
        nodeList = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(nodeList)
        dagPath = om.MDagPath()
        if nodeList.length() == 0:
            print('Please select object!')
        node_iter = om.MItSelectionList(nodeList)
        while not node_iter.isDone():
            node_iter.getDagPath(dagPath)
            model = dagPath.partialPathName()
            self.more_lst = []
            num = 0
            iterator_1 = om.MItMeshPolygon(pm.PyNode(model).__apiobject__())
            while not iterator_1.isDone():
                polygon = iterator_1.polygonVertexCount()
                item = iterator_1.currentItem()
                index = iterator_1.index()
                if polygon > 4:
                    self.more_lst.append(mc.ls(sl=True)[0] + '.f[{0}]'.format(index))
                    num = 1
                else:
                    pass
                iterator_1.next()
            if num == 1:
                print("该模型有多边面！")
                print(self.more_lst)
            else:
                print('该模型没有多边面。')
            node_iter.next()
    def select_illegal(self):
        for item in self.more_lst:
            mc.select(item, add=True)




# 模型坐标轴回归原点

    def method_pivot(self):
        if self.item_4.isChecked() == True:
            self.button_pivot_1.setDisabled(False)
            self.button_pivot_2.setDisabled(False)
        else:
            self.button_pivot_1.setDisabled(True)
            self.button_pivot_2.setDisabled(True)


    def check_pivot(self):
        self.model_select_list = mc.ls(sl = True)
        for model in self.model_select_list:
            model_scalePivot = "{0}.scalePivot".format(model)
            model_rotatePivot = "{0}.rotatePivot".format(model)
            scalePivot_t = mc.xform(model_scalePivot,q = True,t = True)
            rotatePivot_t = mc.xform(model_rotatePivot, q=True, t=True)
            if scalePivot_t[0] != 0:
                print("{0} scalePivot does not return to zero".format(model))
            else:
                if scalePivot_t[1] != 0:
                    print("{0} scalePivot does not return to zero".format(model))
                else:
                    if scalePivot_t[2] != 0:
                        print("{0} scalePivot does not return to zero".format(model))
                    else:
                        print("{0} scalePivot return to zero".format(model))
            if rotatePivot_t[0] != 0:
                print("{0} rotatePivot does not return to zero".format(model))
            else:
                if rotatePivot_t[1] != 0:
                    print("{0} rotatePivot does not return to zero".format(model))
                else:
                    if rotatePivot_t[2] != 0:
                        print("{0}rotatePivot does not return to zero".format(model))
                    else:
                        print("{0} rotatePivot return to zero".format(model))
    def fix_pivot(self):
        for model in self.model_select_list:
            model_transform = mc.xform(model, q=True, t=True, a=True)
            mc.move(model_transform[0], model_transform[1], model_transform[2], "{0}.scalePivot".format(model), a=True)
            mc.move(model_transform[0], model_transform[1], model_transform[2], "{0}.rotatePivot".format(model), a=True)
        print('The model pivot return to zero!')


# 模型回归原点

    def method_model_zero(self):
        if self.item_5.isChecked() == True:
            self.button_mz_1.setDisabled(False)
            self.button_mz_2.setDisabled(False)
        else:
            self.button_mz_1.setDisabled(True)
            self.button_mz_2.setDisabled(True)

    def check_model_zero(self):
        self.mz_select_list = mc.ls(sl = True)
        for model in self.mz_select_list:
            mz_model_transform = mc.xform(model,q = True,t = True)
            if mz_model_transform[0] != 0:
                print("{0} does not return to the origin".format(model))
            else:
                if mz_model_transform[1] != 0:
                    print("{0} does not return to the origin".format(model))
                else:
                    if mz_model_transform[2] != 0:
                        print("{0} does not return to the origin".format(model))
                    else:
                        print("{0} return to the origin".format(model))
    def fix_model_zero(self):
        for model in self.mz_select_list:
            mc.move(0,0,0,model)


# 检查重叠面

    def method_overlap_face(self):
        if self.item_6.isChecked() == True:
            self.button_of_1.setDisabled(False)
            self.button_of_2.setDisabled(False)
            self.button_of_3.setDisabled(True)
        else:
            self.button_of_1.setDisabled(True)
            self.button_of_2.setDisabled(True)
            self.button_of_3.setDisabled(True)

    def check_overlap_face(self):
        nodeList = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(nodeList)
        dagPath = om.MDagPath()
        node_iter = om.MItSelectionList(nodeList)
        self.overlap_name = []
        while not node_iter.isDone():
            node_iter.getDagPath(dagPath)
            model = dagPath.partialPathName()
            face_iterator = om.MItMeshPolygon(pm.PyNode(model).__apiobject__())
            face_dict = {}
            face_name = []
            value_list = []
            while not face_iterator.isDone():
                point_array = om.MPointArray()
                face_iterator.getPoints(point_array)
                point_index = 0
                face_list = []
                while point_index < point_array.length():
                    point = point_array[point_index]
                    point_tup = (point.x, point.y, point.z)
                    face_list.append(point_tup)
                    point_index = point_index + 1
                index = face_iterator.index()
                face = model + ".f[{0}]".format(index)
                face_name.append(face)
                face_dict[face] = face_list
                value_list.append(face_list)
                face_iterator.next()
            for item in face_dict.items():
                norm_name = item[0]
                norm = item[1]
                value_list.pop(0)
                face_name.pop(0)
                norm.sort()
                for coord in value_list:
                    coord.sort()
                    if norm == coord:
                        self.overlap_name.append(norm_name)
                        self.overlap_name.append(face_name[value_list.index(coord)])
                    else:
                        pass
            node_iter.next()
        self.select_list = list(set(self.overlap_name))

        if len(self.select_list) > 0:
            print('Surface of overlap:', self.select_list)
        elif nodeList.length() == 0 and len(self.select_list) == 0:
            print('Please select object!')
        elif nodeList.length() > 0 and len(self.select_list) == 0:
            print('The model has no overlapping surface!')


    def select_overlap_face(self):
        mc.select(clear=True)
        for item in self.select_list:
            mc.select(item, add=True)
        print('The selection is complete!')

    def fix_overlap_face(self):
        pass


# 检查模型面的法线是否正确

    def method_model_normal(self):
        if self.item_7.isChecked() == True:
            self.button_mn_1.setDisabled(False)
            self.button_mn_2.setDisabled(False)
            self.button_mn_3.setDisabled(False)
        else:
            self.button_mn_1.setDisabled(True)
            self.button_mn_2.setDisabled(True)
            self.button_mn_3.setDisabled(True)

    def check_model_normal(self):
        self.face_names = []
        nodeList = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(nodeList)
        dagPath = om.MDagPath()
        if nodeList.length() == 0:
            print('Please select object!')
        node_iter = om.MItSelectionList(nodeList)
        while not node_iter.isDone():
            node_iter.getDagPath(dagPath)
            model = dagPath.partialPathName()
            face_iterator = om.MItMeshPolygon(pm.PyNode(model).__apiobject__())
            mFnMesh = om.MFnMesh(pm.PyNode(model).__apiobject__())
            while not face_iterator.isDone():
                index = face_iterator.index()
                m_vector = om.MVector()
                face_iterator.getNormal(m_vector, om.MSpace.kWorld)
                # 面顶点的索引
                vertices_int = om.MIntArray()
                face_iterator.getVertices(vertices_int)
                point = face_iterator.center(om.MSpace.kWorld)
                point = point + m_vector * 0.1
                #print(m_vector)
                start_point = om.MFloatPoint(point.x, point.y, point.z)
                ray_dir = om.MFloatVector(m_vector)
                hit_point = om.MFloatPointArray()
                iteration = mFnMesh.allIntersections(
                    om.MFloatPoint(start_point),
                    om.MFloatVector(ray_dir),
                    None,
                    None,
                    False,
                    om.MSpace.kWorld, 99999,
                    False,
                    mFnMesh.autoUniformGridParams(),
                    False,
                    hit_point,
                    None,
                    None,
                    None,
                    None,
                    None,
                    0.0001
                )
                if iteration and hit_point.length() % 2 != 0:
                    self.face_names.append("{0}.f[{1}]".format(model, index))

                #print(iteration)
                #print(hit_point.length())
                face_iterator.next()
            node_iter.next()
        if len(self.face_names) != 0:
            print('The wrong surface of the normal：', self.face_names)
        elif len(self.face_names) == 0 and nodeList.length() > 0:
            print('The surface normals of the model are correct!')

    def select_model_normal(self):
        pm.select(clear = True)
        for face in self.face_names:
            pm.select(face,add = True)
        print('Selected Complete!')

    def fix_model_normal(self):
        for normal in self.face_names:
            pm.polyNormal(normal, nm=0, unm=0)
        print('Modify Complete!')


# 模型全封闭，没有洞

    def method_model_hole(self):
        if self.item_8.isChecked() == True:
            self.button_mh_1.setDisabled(False)
            self.button_mh_2.setDisabled(False)
            self.button_mh_3.setDisabled(False)
        else:
            self.button_mh_1.setDisabled(True)
            self.button_mh_2.setDisabled(True)
            self.button_mh_3.setDisabled(True)

    def check_model_hole(self):
        model_select_list = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(model_select_list)
        model_dagPath = om.MDagPath()
        model_iter = om.MItSelectionList(model_select_list)
        self.hole_edge_list = []
        if model_select_list.length() == 0:
            print('Please select object!')
        while not model_iter.isDone():
            model_iter.getDagPath(model_dagPath)
            model = model_dagPath.partialPathName()
            edge_iter = om.MItMeshEdge(pm.PyNode(model).__apiobject__())
            while not edge_iter.isDone():
                face_mIntArray = om.MIntArray()
                edge_iter.getConnectedFaces(face_mIntArray)
                edge_index = edge_iter.index()
                if face_mIntArray.length() < 2:
                    self.hole_edge_list.append('{0}.e[{1}]'.format(model, edge_index))
                edge_iter.next()
            model_iter.next()
        if len(self.hole_edge_list) > 0:
            print('The edge of the model hole:',self.hole_edge_list)
        elif len(self.hole_edge_list) == 0 and model_select_list.length() > 0:
            print('No holes in the model!')


    def select_model_hole(self):
        pm.select(clear=True)
        for edge in self.hole_edge_list:
            pm.select(edge,add=True)
        print('The selection is complete!')
    def fix_model_hole(self):
        for edge in self.hole_edge_list:
            pm.polyCloseBorder(edge, ch=True)
        print('fix completed!')


# 检查模型是否有孤立点

    def method_isolated_vertex(self):
        if self.item_9.isChecked() == True:
            self.button_iv_1.setDisabled(False)
            self.button_iv_2.setDisabled(False)
            self.button_iv_3.setDisabled(False)
        else:
            self.button_iv_1.setDisabled(True)
            self.button_iv_2.setDisabled(True)
            self.button_iv_3.setDisabled(True)

    def check_isolated_vertex(self):
        node_select_list = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(node_select_list)
        node_mDagPath = om.MDagPath()
        node_iter = om.MItSelectionList(node_select_list)
        self.vertex_select_list = []
        if node_select_list.length() == 0:
            print('Please select object!')
        while not node_iter.isDone():
            node_iter.getDagPath(node_mDagPath)
            model = node_mDagPath.partialPathName()
            vertex_iter = om.MItMeshVertex(pm.PyNode(model).__apiobject__())
            while not vertex_iter.isDone():
                vertex_mIntArray = om.MIntArray()
                vertex_iter.getConnectedEdges(vertex_mIntArray)
                if vertex_mIntArray.length() == 0:
                    self.vertex_select_list.append('{}.vtx[{}]'.format(model, vertex_iter.index()))
                vertex_iter.next()
            node_iter.next()
        if len(self.vertex_select_list) > 0:
            print('The model has isolated vertex:', self.vertex_select_list)
        elif len(self.vertex_select_list) == 0 and node_select_list.length() > 0:
            print('The model has no isolated vertex!')

    def select_isolated_vertex(self):
        pm.select(clear=True)
        for vertex in self.vertex_select_list:
            pm.select(vertex, add=True)
        print('The selection is complete!')

    def fix_isolated_vertex(self):
        for vertex in self.vertex_select_list:
            pm.delete(vertex)
        print('The selection is complete!')


# 冻结变换和删除历史

    def method_freeze_delete(self):
        if self.item_10.isChecked() == True:
            self.button_fd_1.setDisabled(False)
            self.button_fd_2.setDisabled(False)

        else:
            self.button_fd_1.setDisabled(True)
            self.button_fd_2.setDisabled(True)


    def freeze_transformations(self):
        node_select_list = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(node_select_list)
        node_mDagPath = om.MDagPath()
        node_iter = om.MItSelectionList(node_select_list)
        if node_select_list.length() == 0:
            print('Please select object!')
        else:
            while not node_iter.isDone():
                # 获取节点的短名
                node_iter.getDagPath(node_mDagPath)
                model = node_mDagPath.partialPathName()
                pm.makeIdentity(model, apply=True, t=1, r=1, s=1, n=0, pn=1)
                print(model, 'has been frozen transformations')
                node_iter.next()

    def delete_history(self):
        node_select_list = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(node_select_list)
        node_mDagPath = om.MDagPath()
        node_iter = om.MItSelectionList(node_select_list)
        if node_select_list.length() == 0:
            print('Please select object!')
        else:
            while not node_iter.isDone():
                # 获取节点的短名
                node_iter.getDagPath(node_mDagPath)
                model = node_mDagPath.partialPathName()
                pm.delete(model, ch=True)
                print(model, 'has been deleted constructionHistory')
                node_iter.next()



def showUI():
    ui = GEO_CHECK_UI()
    ui.show()
    return ui


ui = showUI()

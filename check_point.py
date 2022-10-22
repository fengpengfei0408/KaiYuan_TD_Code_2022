import maya.cmds as mc

if mc.window('main', exists=True):
    mc.deleteUI('main')

mainWindow = mc.window('main', t='check_point', w=400, h=300)
mc.columnLayout()
mc.text(l='选择一个物体检查是否有点重合', w=400, h=50)
coincident_point = mc.button('check', c='check()', w=400, h=100)
mc.showWindow(mainWindow)


def check():
    # 获取检查对象
    model = mc.ls(sl=True)
    mc.select(model[0] + '.vtx[0:]')
    model_list = mc.ls(sl=True, fl=True)
    mc.select(clear=True)

    # 创建字典存储所有的点坐标
    vtxList = {}
    for i in model_list:
        position = mc.xform(i, q=True, ws=True, t=True)
        vtxList[i] = position

    # 无重复点的字典
    checkList = {}
    # 重复点的字典
    coincidentList = {}
    for k, v in vtxList.items():
        if v not in checkList.values():
            checkList[k] = v
        else:
            coincidentList[k] = v

    # 判断重复的点字典的长度，不等于0 则有重复的点
    if len(coincidentList) == 0:
        print '没有重合的点'
    else:
        print '有重合点\n个数：%d:' % (len(coincidentList)), coincidentList
    # 选中重复的点
    for i in coincidentList.keys():
        mc.select(i, add=True)

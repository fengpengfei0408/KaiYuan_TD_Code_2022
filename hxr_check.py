import maya.cmds as mc

s_name_list = []


def checkposition():
    d_value_list = []
    v_dict = {}
    s_list = []
    global s_name_list
    s_name_list = []
    v_name_list = mc.ls(sl=True, fl=True)
    set_list = []
    set_s_list = []
    if v_name_list == []:
        d3 = cmds.confirmDialog(t='判断是否存在重合点', m='没有选中点', button='ok')

    for i in v_name_list:
        v_location = tuple(mc.xform(i, q=True, ws=True, t=True))
        v_dict[i] = v_location

    for i in v_dict.values():
        d_value_list.append(i)
        set_list = set(d_value_list)

    for i in d_value_list:
        if d_value_list.count(i) > 1:
            s_list.append(i)
            set_s_list = list(set(s_list))

    for i in set_s_list:
        k = list(k for k, v in v_dict.items() if v == i)
        s_name_list.append(k)

    if len(set_list) == len(d_value_list):
        d1 = cmds.confirmDialog(t='判断是否存在重合点', m='不存在重合点', button='ok')
        # print('No Superposition')
    else:
        d2 = cmds.confirmDialog(t='判断是否存在重合点', m='存在重合点', button='ok')
        # print('Exist Superposition')

    return s_name_list, win


def selectall():
    global s_name_list
    mc.select(clear=True)
    for i in range(len(s_name_list)):
        mc.select(s_name_list[i], add=True)


def merge():
    mc.polyMergeVertex(mc.ls(sl=True), ch=True)


def combine():
    selects = mc.ls(sl=True)
    i_list = []
    for i in selects:
        i_list.append(i.split('.')[0])
    mc.select(clear=True)
    for i in range(len(i_list)):
        mc.select(i_list[i], add=True)
    mc.polyUnite(ch=True, muv=True, cp=True)


def CreatWin():
    win_name = 'my_win'
    if mc.window(win_name, q=True, exists=True):
        mc.deleteUI(win_name, wnd=True)

    win = mc.window(win_name, t='Check Superposition', w=400, h=400, sizeable=False)
    form = mc.formLayout(nd=100)
    text1 = mc.text(l='第一步必须先按check！')
    text2 = mc.text(l='第二步会选中所有重合点')
    text3 = mc.text(l='第三步会合并物体')
    text4 = mc.text(l='第四步会缝合重合点')
    b_check = mc.button(l='check', w=70, h=40, c='checkposition()')
    b_select_all = mc.button(l='select all', w=70, h=40, c='selectall()')
    b__combine = mc.button(l='combine', w=70, h=40, c='combine()')
    b_merge_super = mc.button(l='merge superposition', w=115, h=40, c='merge()')

    mc.formLayout(form, edit=True,
                  af=[(text1, 'top', 38), (text1, 'left', 50), (b_check, 'top', 25), (text2, 'left', 50),
                      (text3, 'left', 50), (text4, 'left', 50)])
    mc.formLayout(form, edit=True, ac=[(b_check, 'left', 35, text1), (b_select_all, 'top', 20, b_check),
                                       (b_select_all, 'left', 30, text2), (text2, 'top', 50, text1),
                                       (b_select_all, 'left', 30, text2), (text3, 'top', 50, text2),
                                       (text4, 'top', 50, text3), (b__combine, 'top', 20, b_select_all),
                                       (b__combine, 'left', 63, text3), (b_merge_super, 'left', 35, text4),
                                       (b_merge_super, 'top', 25, b__combine)])
    mc.showWindow(win)


CreatWin()




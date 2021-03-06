
#coding=utf-8

from PyQt5.QtWidgets import QListView, QMenu, QAction, QMessageBox
from UI.listModel_history import ListModel

class ListView(QListView):
    map_listview = []
    # map_listview保存QListView对象和分组名称的对应关系

    def __init__(self,ShowModule):
        super().__init__()
        self.m_pModel = ListModel()
        # 必须：设置列表的模型
        self.setModel(self.m_pModel)
        # 传入显示函数
        self.ShowModule = ShowModule
        
    def contextMenuEvent(self, event):
        #重写上下文菜单
        hitIndex = self.indexAt(event.pos()).column()               # 返回鼠标指针相对于接收事件的小部件的位置
        
        if hitIndex > -1:               # 找到索引
            pmenu = QMenu(self)

            pDeleteAct = QAction("打开", pmenu)
            pDeleteAct.triggered.connect(self.OpenModule)
            pmenu.addAction(pDeleteAct)

            pDeleteAct = QAction("删除", pmenu)
            pDeleteAct.triggered.connect(self.deleteItemSlot)
            pmenu.addAction(pDeleteAct)

            pmenu.popup(self.mapToGlobal(event.pos()))      # 显示菜单，以便动作QAction对象在指定的全局位置p处。这里的全局位置p是根据小部件的本地坐标转换为全局坐标的
            

    def OpenModule(self):
        # 打开菜单
        index = self.currentIndex().row()
        if index > -1:
            sm = self.m_pModel.getItem(index)
            self.ShowModule(sm.Get("ModelName"))

    def deleteItemSlot(self):
        '''
        删除
        '''
        index = self.currentIndex().row()
        if index > -1:
            self.m_pModel.deleteItem(index)

    def addItem(self, SimpleModel):
        '''
        新增
        '''
        self.m_pModel.addItem(SimpleModel)

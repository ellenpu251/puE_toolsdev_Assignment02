import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance

def maya_main_window():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)

class SmartUI(QtWidgets.QDialog):

    def __init__(self):
        super(SmartUI,self).__init__(parent=maya_main_window())
        self.setWindowTitle("Smart UI")
        self.resize(500,200)
        self.setWindowFlags(self.windowFlags()^QtCore.QtWindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.title_lbl = QtWidgets.QLabel("Smart Save")
        self.title_lbl.setStyleSheet("font: bold 40px")
        self.dir_le = QtWidgets.QLabel("Directory")
        self.dir_le = QtWidgets.QLineEdit()
        self.browse_btn = QtWidgets.QPushButton("Browse")
        self.save_btn = QtWidgets.QPushButton("Save")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

    def create_layout(self):
         self.directory_lay = QtWidgets.QHBoxLayout()
         self.directory_lay.addWidget(self.dir_lbl)
         self.directory_lay.addWidget(self.dir_le)
         self.directory_lay.addWidget(self.browse_btn)

         self.bottom_btn_lay = QtWidgets.QHBoxLayout()
         self.bottom_btn_lay.addWdiget(self.save_btn)
         self.browse_btn_lay.addWidget(self.cancel_btn)

         self.main_layout = QtWidgets.QVBoxLayout()
         self.main_layout.addWidget(self.title_lbl)
         self.main_layout.addLayout(self.directory_lay)
         self.main_layout.addLayout(self.bottom_btn_lay)

         self.setLayout(self.main_layout)

